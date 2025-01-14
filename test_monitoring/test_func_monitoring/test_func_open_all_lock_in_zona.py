# Мoниторинг. Зона. Открыть - По статусу - Все ячейки

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config import name_zone_publ
from time import sleep
from termcolor import cprint


def open_lock_all(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    cprint("Мoниторинг. Зона. Открыть - По статусу - Все ячейки / test_func_open_all_lock_in_zona", "yellow")

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # Открыть зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()

    # количество ячеек
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"В зоне '{name_zone_publ}' кол-во ячеек: {len(cells)}")

    # Нажимаем Открыть
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Открыть']"))).click()

    # По статусу
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'по статусу']"))).click()

    # Выбрать все ячейки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать статус ячейки']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Все']"))).click()

    # Открыть
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()= 'Открыть'])[2]"))).click()
    actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
    sleep(3)

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")


    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101, 201}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                print()

def test_open_lock_all(browser):
    open_lock_all(browser)
