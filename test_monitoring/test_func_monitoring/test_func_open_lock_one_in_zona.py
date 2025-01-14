# Мoниторинг. Зона. Открыть - одну ячейку

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config import name_zone_publ
from termcolor import cprint
from time import sleep
import random


def click_empty_space(browser):
    actions = ActionChains(browser)
    actions.move_by_offset(0, 0).click().perform()

def open_lock_one(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    cprint("Мoниторинг. Зона. Открыть - одну ячейку / test_func_open_lock_one_in_zona", "yellow")

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # Открыть зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()
    sleep(0.1)

    lock_all = browser.find_elements(By.CLASS_NAME, "lock-item-container")
    closed_locks = []
    open_locks = []

    for l in lock_all:
        status = l.find_element(By.XPATH, ".//div[@class='icon']")
        status_text = status.get_attribute("aria-label")
        lock_name = l.find_element(By.XPATH, ".//div[@class='title']//div[@class='title']").text
        lock_number = lock_name.replace("Ячейка ", "").strip()

        if status_text == "Закрыт":
            closed_locks.append(lock_number)
        elif status_text == "Открыт":
            open_locks.append(lock_number)

    if closed_locks:
        lock_to_closed = random.choice(closed_locks)

        # Нажимаем Открыть
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Открыть']"))).click()

        # Выбираем "ячейку"
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'ячейку']"))).click()

        # Вводим номер ячейки
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id= 'Номер ячейки']"))).send_keys(lock_to_closed)

        # Открыть
        browser.find_element(By.XPATH, "(//button[text()= 'Открыть'])[2]").click()
        actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
        sleep(2)
        print(f"Открыта ячейка '{lock_to_closed}'")

        # Получаю текст уведомления
        notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
        if notifications:
            last_notification_text = notifications[-1].text
            print(f"Текст уведомления: {last_notification_text}")

    else:
        if open_locks:
            lock_to_open = random.choice(open_locks)

            # Нажимаем Открыть для открытого замка
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Открыть']"))).click()

            # Выбираем "ячейку"
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'ячейку']"))).click()

            # Вводим номер открытого замка
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id= 'Номер ячейки']"))).send_keys(lock_to_open)

            # Открыть
            browser.find_element(By.XPATH, "(//button[text()= 'Открыть'])[2]").click()
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            sleep(2)
            print(f"Открыта ячейка '{lock_to_open}'")

            # Получаю текст уведомления
            notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
            if notifications:
                last_notification_text = notifications[-1].text
                print(f"Текст уведомления: {last_notification_text}")

    click_empty_space(browser)

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101, 201}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                print()


def test_open_lock_one(browser):
    open_lock_one(browser)
