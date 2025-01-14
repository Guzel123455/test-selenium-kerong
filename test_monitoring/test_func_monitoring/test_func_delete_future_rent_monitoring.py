# Мониторинг. Зона. Выбрать свободную ячейку. Создать аренду на следующий день, удалить

from selenium.common import NoSuchElementException
from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime, timedelta
from selenium.webdriver.common.action_chains import ActionChains
from config import name_zone_publ
from termcolor import cprint


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.1)

def delete_future_rent_monitoring(browser):
    wait = WebDriverWait(browser, 5)
    actions = ActionChains(browser)


    cprint("Мониторинг. Зона. Выбрать свободную ячейку. Создать аренду на следующий день / test_func_future_rent_monitoring", "yellow")

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()

    # Все ячейки
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"В зоне '{name_zone_publ}' кол-во ячеек: {len(cells)}")

    found_free_cell = False
    for cell in cells:
        try:
            failure = cell.find_elements(By.XPATH, ".//div[@class ='failure']")

            if not failure:
                found_free_cell = True

                # номер первой найденной свободной ячейки
                cell_title = cell.find_element(By.CLASS_NAME, "title")
                cell_title_1 = cell_title.text
                print(f"Номер первой в списке свободной ячейки '{cell_title_1}'")

                # клик на "создать аренду"
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Создать аренду']"))).click()
                sleep(1)

                # выбрать идентификатор
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label = 'Open']"))).click()
                sleep(1)
                type = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul:nth-child(1) li")))
                type_1 = type.text
                type.click()
                sleep(1)

                # Преобразование type_1 для сравнения
                type_1_parts = type_1.split(' (')
                if len(type_1_parts) == 2:
                    type_1 = f"({type_1_parts[1].rstrip(')')}) {type_1_parts[0].strip()}"

                # ввести номер ячейки
                num = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Введите номер ячейки']")))
                num.send_keys(cell_title_1)
                sleep(1)

                # Начало периода
                # клик на календарь
                wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw']"))).click()
                # клик на текущую дату
                wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class = 'MuiButtonBase-root MuiPickersDay-root Mui-selected MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()
                sleep(1)

                # Получение даты начала
                start_date_input = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[1]")))
                start_date_str = start_date_input.get_attribute("value")
                start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
                sleep(1)

                # Конец периода: добавление одного дня к начальной дате
                end_date = start_date + timedelta(days=2)

                # Задаем новую дату
                new_end_date_str = end_date.strftime("%d.%m.%Y")

                # начало
                start_date = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@ placeholder = 'ДД.ММ.ГГГГ'])[1]")))
                start_date.click()
                # удаляем текущую дату
                start_date.send_keys(Keys.CONTROL, 'a')
                start_date.send_keys(Keys.DELETE)
                # установить дату след.дня
                start_date_input.send_keys(new_end_date_str)

                # конец
                end_date_input = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@ placeholder = 'ДД.ММ.ГГГГ'])[2]")))
                end_date_input.click()
                end_date_input.send_keys(new_end_date_str)

                # начальное время
                input_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,"(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[2]")))
                input_element.click()
                input_value = input_element.get_attribute("value")
                hours, minutes = map(int, input_value.split(':'))

                # +1 час от начального времени
                hours += 1
                if hours == 24:
                    hours = 0
                new_time = f"{hours:02}:{minutes:0}"

                # конечное время
                time_end = wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[4]")))
                time_end.click()
                time_end.send_keys(new_time)

                # Создать аренду
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text() = 'Создать аренду'])[2]"))).click()
                sleep(1)

                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}")

                text_2 = 'Добавление доступа к существующей аренде'
                try:
                    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h2[text() = 'Добавление доступа к существующей аренде']"), text_2))

                    # Если текст совпадает, кликнуть на кнопку для закрытия окна
                    # if text_2 in browser.find_element(By.XPATH, "//h2[text() = 'Добавление доступа к существующей аренде']").text:
                    button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Хорошо']")))
                    browser.execute_script("arguments[0].click();", button)
                    print("В выбранной ячейки уже создана аренда на данный период времени и даты, переходим к следующей")
                    print()

                    continue

                except Exception as e:
                    print()

                for request in browser.requests:
                    if request.response:
                        if request.response.status_code not in {200, 101}:
                            error_message = request.response.body.decode('utf-8')
                            print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

                print(f"Создана аренда на '{cell_title_1.replace('\n', ' ')}' с идентификатором '{type_1}'. Период аренды: {new_end_date_str} с {input_value} до {new_time}")

                # проверить созданную аренду
                # открыть ячейку
                cell_title.click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Будущие аренды']"))).click()
                sleep(0.2)

                # дата и время созданной аренды
                your_rental_start = f"{new_end_date_str} | {input_value}:00"

                # все строки в "будущей аренде"
                rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr")))

                # Проходим по каждой строке
                for index, row in enumerate(rows):
                    # Получаем первую ячейку с датой и временем начала периода
                    try:

                        # дата начала
                        start_period = row.find_element(By.XPATH, ".//td[1]/h2").text.strip()
                        # идентификатор
                        identifier = row.find_element(By.XPATH, ".//td[3]").text.strip()

                        # Поиск совпадений
                        if start_period == your_rental_start:
                            if identifier == type_1:
                                print(f"Созданная аренда найдена на строке {index + 1}: {start_period} с идентификатором '{identifier}'")

                                # Прокрутка до данной строки
                                scroll_to_element(browser, row)

                                # Удалить аренду
                                delete_button = row.find_element(By.CSS_SELECTOR,"svg > path[d='M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6zM19 4h-3.5l-1-1h-5l-1 1H5v2h14z']")
                                delete_button.click()

                                rental_start_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h5[text()[contains(., 'Начало аренды')]]"))).text
                                print(f"Удаляется аренда: '{rental_start_text}'")
                                sleep(1)

                                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Снять аренду']"))).click()
                                sleep(1)
                                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()

                                # Получаю текст уведомления
                                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                                if notifications:
                                    last_notification_text = notifications[-1].text
                                    print(f"Текст уведомления: {last_notification_text}")
                                    break

                    except NoSuchElementException:
                        print(f"В строке  нет данных для даты и времени начала периода")
                break

        except Exception:
            continue


    if not found_free_cell:
        print("Нет доступных ячеек для аренды")


def test_delete_future_rent_monitoring(browser):
    delete_future_rent_monitoring(browser)