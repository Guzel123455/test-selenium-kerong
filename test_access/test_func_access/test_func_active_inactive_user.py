# Права доступа. Активные / Неактивные пользователи

from selenium.common import TimeoutException
from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import cprint
from time import sleep

from test_access.access_locators import Locator


def active_inactive_user(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Права доступа. Активные / Неактивные пользователи / test_func_active_inactive_user", "yellow")

    # Клик по кнопке Настройки
    wait.until(EC.element_to_be_clickable((Locator.SETTINGS_BUTTON))).click()
    wait.until(EC.element_to_be_clickable((Locator.ACCESS_BUTTON))).click()
    sleep(0.5)

    # получить список активных пользователей
    list_login = []
    while True:
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            login = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
            login_text = login.text
            if login_text:
                list_login.append(login_text)
        try:
            next_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label = 'Go to next page']")))
            next_page.click()
            sleep(0.2)
        except TimeoutException:
            break

    active_user_count = len(list_login)
    print(f"Количество активных пользователей: {active_user_count}")
    print(f"Все активные логины: {list_login}")
    print()

    # получить список неактивных пользователей
    wait.until(EC.element_to_be_clickable((Locator.INACTIVE_USER))).click()

    line = wait.until(EC.visibility_of_element_located(Locator.COUNT_LINES))
    line_text = line.text
    inactive_count = line_text.split("из")[-1].strip()
    print(f"Количество неактивных пользователей: {inactive_count}")



def test_active_inactive_user(browser):
    active_inactive_user(browser)