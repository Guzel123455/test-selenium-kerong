# добавление соединения керонг апи

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from config import address_input, port_api
from browser_setup import browser

def auth_kerong(browser):
    wait = WebDriverWait(browser, 10)

        # клик на настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Настройки']"))).click()

        # клик по разделу kerong api
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class  = 'settings-item'])[2]"))).click()

        # клик по кнопке Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Добавить']"))).click()

        # ввести адрес
    address = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id= 'outlined-basic'])[2]")))
    address.send_keys(Keys.BACKSPACE * 5)
    address.send_keys(address_input)

        # ввести порт
    port = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id= 'outlined-basic'])[3]")))
    port.send_keys(Keys.BACKSPACE * 5)
    port.send_keys(port_api)
    print(f"Создано соединение {address_input}")

        # Использовать по умолчанию
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='MuiSwitch-thumb css-19gndve']")))
    browser.execute_script("arguments[0].click();", checkbox)
    time.sleep(0.1)

    action = ActionChains(browser)
    for _ in range(3):
        action.click(checkbox)
    action.perform()
    time.sleep(0.1)

        # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class= 'UIbutton'])[4]"))).click()

        # Проверка состояния Используется
    is_used = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text() = 'Используется']")))
    is_used_text = is_used.text.strip()

    if is_used_text == "Используется":

            # синхронизировать
        browser.find_element(By.XPATH, "(//button[@class='UIbutton'])[2]").click()
        time.sleep(2)
        print("Состояние- Используется, Синхронизировано")
        print()

    else:
            # строка с соединением
        wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[@class='MuiTableRow-root css-1axy92l']"))).click()

            # кнопка редактировать
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='UIbutton'])[3]"))).click()

            # использовать по умолчанию
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class= 'MuiSwitch-thumb css-19gndve']")))
        browser.execute_script("arguments[0].click();", button)

        action = ActionChains(browser)
        for _ in range(2):
            action.click(button)
        action.perform()

            # сохранить
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
        if is_used_text != "Используется":
            print("Не используется")

            # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                pytest.fail()

def test_auth_kerong(browser):
    auth_kerong(browser)