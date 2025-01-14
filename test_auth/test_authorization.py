# авторизация

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import servername, port_auth, log_in, password
from browser_setup import browser

def authorization(browser):
    wait = WebDriverWait(browser, 10)

    # нажать кнопку database
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='server-btn']"))).click()

    # найти поле адрес сервера, очистить, ввести адрес сервера
    server = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Адрес сервера']")))
    server.send_keys(Keys.BACKSPACE * 15)
    server.send_keys(servername)

    # найти поле Порт, очистить, ввести верный порт
    port = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Порт сервера']")))
    port.send_keys(Keys.BACKSPACE * 4)
    port.send_keys(port_auth)

    # Сохранить данные
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить данные']"))).click()

    # ввести логин
    login = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Логин']")))
    login.send_keys(log_in)

    # ввести пароль
    passw = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Пароль']")))
    passw.send_keys(password)

    # клик по кнопке войти
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class= 'UIbutton']"))).click()
    time.sleep(0.5)

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200,101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")


def test_authorization(browser):
    authorization(browser)