# Мoниторинг - Зона. Открытие одной ячейки
import random
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import name_zone_text
from browser_setup import browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def click_empty_space(browser):
    actions = ActionChains(browser)
    actions.move_by_offset(0, 0).click().perform()

def open_lock_some(browser):
    wait = WebDriverWait(browser, 20)
    actions = ActionChains(browser)

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # Открыть зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_text}']"))).click()
    time.sleep(0.1)

    lock_all = browser.find_elements(By.CLASS_NAME, "lock-item-container")
    locks_num = []

    # получаем список ячеек
    for l in lock_all:
        lock_name = l.find_element(By.XPATH, ".//div[@class='title']//div[@class='title']").text
        lock_number = lock_name.replace("Ячейка ", "").strip()
        locks_num.append(lock_number)

    # выбираем ячейку От и До
    if locks_num:
        lock_start = random.choice(locks_num[0])
        lock_stop = str(int(lock_start) + 2)

        # Нажимаем Открыть
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Открыть']"))).click()

        # Выбираем "ячейку"
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'несколько']"))).click()

        # Номер ячейки C
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id= 'outlined-basic'])[2]"))).send_keys(lock_start)
        # Номер ячейки ПО
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id= 'outlined-basic'])[3]"))).send_keys(lock_stop)

        # Открыть
        browser.find_element(By.XPATH, "(//button[text()= 'Открыть'])[2]").click()
        time.sleep(5)

        actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
        time.sleep(0.2)

        print(f"Открыты ячейки с {lock_start} по {lock_stop}")

    click_empty_space(browser)
    time.sleep(1)

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101, 201}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
 #               pytest.fail()

def test_open_lock_some(browser):
    open_lock_some(browser)
