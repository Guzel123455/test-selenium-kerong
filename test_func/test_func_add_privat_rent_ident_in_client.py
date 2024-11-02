# Добавить доступ к ячейкам ПО ИДЕНТИФИКАТОРУ в карточке клиента

import time
from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import name_zone_private, num_from_private, num_to_private


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.5)

def add_privat_rent_ident_in_client(browser):
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 10)

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # Поиск клиента у которого привязан идентификатор
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    for row in rows:
        ident = row.find_element(By.CSS_SELECTOR, "td:nth-child(3) h2")
        ident_text = ident.text.strip()

        # открытие клиента и выбор идентифкатора
        if ident_text != '':
            # имя клиента
            name = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h4")
            print(f"Выбран клиент '{name.text}' с идентификатором '{ident_text}'")
            actions.move_to_element(row).click().perform()
            time.sleep(0.1)

            # открыть вкладку Доступ к ячейкам
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Доступ к ячейкам']"))).click()
            time.sleep(0.1)

            # добавить доступ
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить доступ']"))).click()
            time.sleep(0.1)

            # Выбрать тип аренды
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'demo-simple-select-helper']"))).click()
            time.sleep(0.1)

            # по идентификатору
            wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'По идентификатору']"))).click()
            time.sleep(0.1)

            # выбрать идентификатор
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'demo-simple-select-helper'])[2]"))).click()
            time.sleep(0.1)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul:nth-child(1) li"))).click()
            time.sleep(0.1)

            # выбрать зону
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'demo-simple-select-helper'])[3]"))).click()
            zona = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text() = '{name_zone_private} [{num_from_private} - {num_to_private}]']")))
            browser.execute_script("arguments[0].scrollIntoView(true);", zona)
            wait.until(EC.element_to_be_clickable(zona)).click()
            time.sleep(0.1)

            # ввести номер ячейки
            num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[6]")))
            num.send_keys('1')
            time.sleep(0.1)

            # Начало периода
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw']"))).click()
            time.sleep(0.1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()
            time.sleep(0.1)

            # Конец периода
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw'])[2]"))).click()
            time.sleep(0.1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()
            time.sleep(0.1)

            # начальное время
            input_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[2]")))
            input_element.click()
            input_value = input_element.get_attribute("value")
            hours, minutes = map(int, input_value.split(':'))
            hours += 1
            if hours == 24:
                hours = 0
            new_time = f"{hours:02}:{minutes:02}"
            time.sleep(0.1)

            # конечное время
            time_end = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[4]")))
            time_end.click()
            time_end.send_keys(new_time)
            time.sleep(0.1)

            # сохранить
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
            time.sleep(0.1)

            # Получаю текст уведомление
            text_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id= 'notistack-snackbar']")))
            text_message_txt = text_message.text
            print(f"Текст уведомления: {text_message_txt}")
            time.sleep(0.1)
            break

        for request in browser.requests:
            if request.response:
                if request.response.status_code not in {200, 101}:
                    error_message = request.response.body.decode('utf-8')
                    print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    try:
        next_page = browser.find_element(By.XPATH, "//button[@aria-label='Go to next page']")
        next_page.click()
            # Рекурсивный вызов функции
        return add_privat_rent_ident_in_client(browser)
    except:
        return False


def test_add_privat_rent_ident_in_client(browser):
    add_privat_rent_ident_in_client(browser)