# Клиенты. Открыть карточку клиента. Добавить доступ в корп зону

from time import sleep
from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import name_zone_corp,num_from_corp, num_to_corp
from datetime import datetime, timedelta
from termcolor import cprint


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.1)

def access_corporate_zone(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Открыть карточку клиента. Добавить доступ в корп зону / test_func_access_corporate_zone", "yellow")

    # открыть вкладку Доступ к зонам
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Доступ к зонам']"))).click()

    # добавить доступ
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить доступ']"))).click()

    # выбрать идентификатор
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id= 'Выбрать идентификатор']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//ul/li"))).click()

    # выбрать зону
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id= 'Выбрать зону']"))).click()
    zona = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{name_zone_corp} [{num_from_corp} - {num_to_corp}]')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", zona)
    zona.click()

    # Начало периода
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class = 'MuiButtonBase-root MuiPickersDay-root Mui-selected MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()

    # Получение даты начала
    start_date_input = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[contains(@class, 'MuiInputBase-input')][1])[7]")))
    start_date_str = start_date_input.get_attribute("value")
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
    # Конец периода: добавление одного дня к начальной дате
    end_date = start_date + timedelta(days=1)

    # Задаем новую конечную дату
    new_end_date_str = end_date.strftime("%d.%m.%Y")
    end_date_input = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@ placeholder = 'ДД.ММ.ГГГГ'])[2]")))
    end_date_input.click()
    end_date_input.send_keys(new_end_date_str)

    print(f"Добавлен доступ к корп.зоне с '{start_date_str}' по '{new_end_date_str}'")

    # сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(1)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текс уведомления: {last_notification_text}")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")



def test_access_corporate_zone(browser):
    access_corporate_zone(browser)
