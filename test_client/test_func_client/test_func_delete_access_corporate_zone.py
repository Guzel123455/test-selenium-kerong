# Клиенты. Карточка клиента. Удалить доступ в корп зону

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from termcolor import cprint

def delete_access(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Карточка клиента. Удалить доступ в корп зону / test_func_delete_access_corporate_zone", "yellow")

    # удалить
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg > path[d='M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6zM19 4h-3.5l-1-1h-5l-1 1H5v2h14z']"))).click()
    sleep(1)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

def test_delete_access(browser):
    delete_access(browser)