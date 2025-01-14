# Мониторинг. Зона. Добавить аренду к существ.аренде

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config import name_zone_publ
from datetime import datetime
from termcolor import cprint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



def double_rental(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    cprint("Мониторинг. Зона. Добавить аренду к существ.аренде / test_func_double_rental", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[5]"))).click()
    id_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//tbody//tr//td/h2)[1]"))).text
    id_2 =  wait.until(EC.element_to_be_clickable((By.XPATH, "(//tbody//tr//td/h2)[2]"))).text
    id_all = f"{id_2}; {id_1}"

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()
    sleep(1)

    # Все ячейки
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"В зоне '{name_zone_publ}' кол-во ячеек: {len(cells)}")

    free_cell_found = False
    cell_title = ""

    for cell in cells:
        try:
            free_status = cell.find_element(By.XPATH, ".//div[@class='free']").text
            if free_status == "Свободен":
                free_cell_found = True

                # номер первой найденной свободной ячейки
                cell_title = cell.find_element(By.CLASS_NAME, "title").text
                print(f"Номер первой в списке свободной ячейки '{cell_title}'")

                # клик на "создать аренду"
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Создать аренду']"))).click()

                # выбрать идентификатор
                a = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class= 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-1uvydh2' ]")))
                a.send_keys(id_1)
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul:nth-child(1) li"))).click()
                sleep(1)

                # ввести номер ячейки
                num = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Введите номер ячейки']")))
                num.send_keys(cell_title)

                # Настройка времени
                # Начало периода
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw']"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class = 'MuiButtonBase-root MuiPickersDay-root Mui-selected MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()

                # Конец периода
                wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw'])[2]"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()

                # начальное время
                input_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,"(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[2]")))
                input_element.click()
                input_value = input_element.get_attribute("value")
                hours, minutes = map(int, input_value.split(':'))

                # +1 час от начального времени
                hours += 1
                if hours == 24:
                    hours = 0
                new_time = f"{hours:02}:{minutes:02}"

                # конечное время
                time_end = wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[4]")))
                time_end.click()
                time_end.send_keys(new_time)

                # Создать аренду
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text() = 'Создать аренду'])[2]"))).click()
                sleep(1)

                # Получение текущей даты и времени
                current_datetime = datetime.now().strftime("%d.%m.%Y")
                print(f"Создана аренда на ячейку '{cell_title}', на {current_datetime} с {input_value} по {new_time}")

                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}")

                break

        except Exception:
            continue


    if not free_cell_found:
        print("Все ячейки заняты")
        return


        # ДОБАВИТЬ АРЕНДУ К СУЩЕСТВ.АРЕНДЕ
    # клик на "создать аренду"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Создать аренду']"))).click()

    # выбрать идентификатор
    a = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@class= 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-1uvydh2' ]")))
    a.send_keys(id_2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul:nth-child(1) li"))).click()
    sleep(1)

    # ввести номер ячейки
    num = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Введите номер ячейки']")))
    num.send_keys(cell_title)

    # Начало периода
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class = 'MuiButtonBase-root MuiPickersDay-root Mui-selected MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()

    # Конец периода
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw'])[2]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class = 'MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()

    # начальное время
    input_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[2]")))
    input_element.click()
    input_value = input_element.get_attribute("value")
    hours, minutes = map(int, input_value.split(':'))

    # +1 час от начального времени
    hours += 1
    if hours == 24:
        hours = 0
    new_time = f"{hours:02}:{minutes:02}"

    # конечное время
    time_end = wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[4]")))
    time_end.click()
    time_end.send_keys(new_time)

    # Создать аренду
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text() = 'Создать аренду'])[2]"))).click()
    sleep(1)

    text_2 = "Добавление доступа к существующей аренде"

    try:
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h2[text() = 'Добавление доступа к существующей аренде']"), text_2))

        # Если текст совпадает, кликнуть на кнопку
        if text_2 in browser.find_element(By.XPATH,"//h2[text() = 'Добавление доступа к существующей аренде']").text:
            button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Добавить']")))
            browser.execute_script("arguments[0].click();", button)
            sleep(1)

            # Получение текущей даты и времени
            current_datetime = datetime.now().strftime("%d.%m.%Y")
            print(f"Создана аренда на ячейку '{cell_title}', на {current_datetime} с {input_value} по {new_time}")

    except Exception as e:
        # Получение текущей даты и времени
        current_datetime = datetime.now().strftime("%d.%m.%Y")
        print(f"Создана аренда на ячейку '{cell_title}', на {current_datetime} с {input_value} по {new_time}")

        # Ищем ячейку по номеру (cell_title)
    for cell in cells:
        cell_title_found = cell.find_element(By.CLASS_NAME, "title").text
        if cell_title_found == cell_title:
            # Если ячейка найдена, кликнем на неё
            cell.click()
            sleep(2)

            a = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id= 'Идентификатор']")))
            input_value = a.get_attribute('value')
            if input_value == id_all:
                print(f"Идентификаторы совпадают")
            else:
                print(f"Идентификаторы не совпадают")

            # сброс
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()



    for request in browser.requests:
            if request.response:
                if request.response.status_code not in {200, 101, 201}:
                    error_message = request.response.body.decode('utf-8')
                    print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

def test_double_rental(browser):
    double_rental(browser)