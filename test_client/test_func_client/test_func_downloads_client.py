# Клиенты. Загрузка файла

from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
from time import sleep

def downloads_client(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Загрузка файла / test_func_downloads_client", "yellow")

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # клик на принтер
    browser.find_element(By.CLASS_NAME, "printer-button").click()
    sleep(1)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
#                pytest.fail()


def test_downloads_client(browser):
    downloads_client(browser)