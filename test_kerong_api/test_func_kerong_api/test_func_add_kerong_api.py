# Kerong Api. Добавление соединения

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config import address_input, port_api
from time import sleep
from termcolor import cprint


def add_kerong(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Kerong Api. Добавление соединения / test_func_add_kerong_api", "yellow")

    # клик на настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Настройки']"))).click()

    # клик по разделу kerong api
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class  = 'settings-item'])[2]"))).click()

    # клик по кнопке Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Добавить']"))).click()

    # ввести адрес
    address = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id= 'Адрес']")))
    address.send_keys(Keys.BACKSPACE * 5)
    address.send_keys(address_input)

    # ввести порт
    port = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id= 'Порт']")))
    port.send_keys(Keys.BACKSPACE * 5)
    port.send_keys(port_api)
    print(f"Создано соединение {address_input}")

    # Использовать по умолчанию
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='MuiSwitch-thumb css-19gndve']")))
    browser.execute_script("arguments[0].click();", checkbox)
    sleep(0.1)

    action = ActionChains(browser)
    for _ in range(3):
        action.click(checkbox)
    action.perform()
    sleep(0.1)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class= 'UIbutton'])[4]"))).click()
    sleep(0.5)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")


    # Проверка состояния Используется
    is_used = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text() = 'Используется']")))
    is_used_text = is_used.text.strip()
    sleep(0.1)

    if is_used_text == "Используется":

        # синхронизировать
        browser.find_element(By.XPATH, "(//button[@class='UIbutton'])[2]").click()
        sleep(0.5)
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
#                pytest.fail()

def test_add_kerong(browser):
    add_kerong(browser)