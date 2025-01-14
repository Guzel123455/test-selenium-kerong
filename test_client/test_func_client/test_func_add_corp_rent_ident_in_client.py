# Клиенты. Открыть карточку клиента. Добавить доступ к ячейкам на корп.зону, по идентификатору


from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
from datetime import datetime
from termcolor import cprint
from config import name_zone_corp, num_from_corp, num_to_corp


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.5)

def add_corp_rent_ident_in_client(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Открыть карточку клиента. Добавить доступ к ячейкам на корп.зону, по идентификатору / test_func_add_corp_rent_ident_in_client", "yellow")

    # открыть вкладку Доступ к ячейкам
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Доступ к ячейкам']"))).click()

    # добавить доступ
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить доступ']"))).click()

    # Выбрать тип аренды
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать тип аренды ']"))).click()

    # по идентификатору
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'По идентификатору']"))).click()

    # выбрать идентификатор
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать идентификатор']"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul:nth-child(1) li"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать зону']"))).click()
    zona = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text() = '{name_zone_corp} [{num_from_corp} - {num_to_corp}]']")))
    browser.execute_script("arguments[0].scrollIntoView(true);", zona)
    wait.until(EC.element_to_be_clickable(zona)).click()

    # Случайный номер ячейки из диапазона
    random_cell_number = random.randint(int(num_from_corp), int(num_to_corp))
    # ввести номер ячейки
    num = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Введите номер ячейки']")))
    num.send_keys(str(random_cell_number))

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
    time_end = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[4]")))
    time_end.click()
    time_end.send_keys(new_time)

    # сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(1)

    # Получение текущей даты и времени
    current_datetime = datetime.now().strftime("%d.%m.%Y")
    print(f"Создана аренда на ячейку '{random_cell_number}', на {current_datetime} с {input_value} по {new_time}")

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

def test_add_corp_rent_ident_in_client(browser):
    add_corp_rent_ident_in_client(browser)