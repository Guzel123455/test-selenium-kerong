# Мониторинг. Открыть ячейку

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
from config import name_zone_publ, num_from_publ, num_to_publ
from time import sleep


def open_lock(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Мониторинг. Открыть ячейку / test_func_open_lock", "yellow")

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # клик "открыть ячейку"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Открыть ячейку']"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать зону']"))).click()
    z = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{name_zone_publ} [{num_from_publ} - {num_to_publ}]')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", z)
    browser.execute_script("arguments[0].click();", z)

    # ввести номер ячейки
    cell = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Номер ячейки']")))
    cell.click()
    cell.send_keys(num_from_publ)

    # открыть
    browser.find_element(By.XPATH, "//button[text()= 'Открыть']").click()
    sleep(2)

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")


def test_open_lock(browser):
    open_lock(browser)

