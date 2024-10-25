# Мoниторинг - Зона. Открытие одной ячейки

import random
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from config import name_zone_text
from browser_setup import browser

def click_empty_space(browser):
    actions = ActionChains(browser)
    actions.move_by_offset(0, 0).click().perform()

def open_lock_one(browser):
    wait = WebDriverWait(browser, 20)
    actions = ActionChains(browser)

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # Открыть зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_text}']"))).click()
    time.sleep(0.1)

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
        lock_to_open = random.choice(closed_locks)

        # Нажимаем Открыть
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Открыть']"))).click()

        # Выбираем "ячейку"
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'ячейку']"))).click()

        # Вводим номер ячейки
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id= 'outlined-basic'])[2]"))).send_keys(lock_to_open)

        # Открыть
        browser.find_element(By.XPATH, "(//button[text()= 'Открыть'])[2]").click()
        print("Ячейка открыта")
        time.sleep(1)

        text_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id= 'notistack-snackbar']")))
        text_message_txt = text_message.text
        print(f"Текст уведомления: {text_message_txt}")

        actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
        time.sleep(0.2)

    else:
        if open_locks:
            lock_to_open = random.choice(open_locks)

            # Нажимаем Открыть для открытого замка
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Открыть']"))).click()

            # Выбираем "ячейку"
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'ячейку']"))).click()

            # Вводим номер открытого замка
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id= 'outlined-basic'])[2]"))).send_keys(lock_to_open)

            # Открыть
            browser.find_element(By.XPATH, "(//button[text()= 'Открыть'])[2]").click()
            time.sleep(1)

            text_message1 = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id= 'notistack-snackbar']")))
            text_message_txt1 = text_message1.text
            print(f"Текст уведомления: {text_message_txt1}")

            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            time.sleep(0.2)

    click_empty_space(browser)
    time.sleep(1)

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101, 201}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
 #               pytest.fail()


def test_open_lock_one(browser):
    open_lock_one(browser)
