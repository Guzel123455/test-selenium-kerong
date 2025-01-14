# Отчеты. Журнал событий. Таблица. Печать данных

from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
from test_reports.reports_locators import Locator
from time import sleep

def event_log_download(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Отчеты. Журнал событий. Таблица. Печать данных / test_func_event_log_DOWNLOAD", "yellow")

    # отчеты
    wait.until(EC.visibility_of_element_located((Locator.REPORTS_BUTTON))).click()

    # журнал событий
    wait.until(EC.visibility_of_element_located((Locator.EVENT_LOG_BUTTON))).click()

    # таблица
    wait.until(EC.visibility_of_element_located((Locator.TABLE_BUTTON))).click()

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


def test_event_log_download(browser):
    event_log_download(browser)