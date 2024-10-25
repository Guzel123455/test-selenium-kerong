# авторизация

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import servername, port_auth, log_in, password
from browser_setup import browser


def authorization(browser):
    wait = WebDriverWait(browser, 10)

    # нажать кнопку "монетки"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='server-btn']"))).click()

    # найти поле адрес сервера, очистить, ввести логин
    server = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='outlined-basic'])[2]")))
    server.send_keys(Keys.BACKSPACE * 15)
    server.send_keys(servername)

    # найти поле Порт, очистить, ввести верный порт
    port = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='outlined-basic'])[3]")))
    port.send_keys(Keys.BACKSPACE * 4)
    port.send_keys(port_auth)

    # Сохранить данные
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить данные']"))).click()

    # ввести логин
    login = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='outlined-basic']")))
    login.send_keys(log_in)

    # ввести пароль
    passw = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='outlined-adornment-password']")))
    passw.send_keys(password)

    # клик по кнопке войти
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class= 'UIbutton']"))).click()
    time.sleep(0.5)
    print("Успешная авторизация")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200,101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                pytest.fail()

def test_authorization(browser):
    authorization(browser)