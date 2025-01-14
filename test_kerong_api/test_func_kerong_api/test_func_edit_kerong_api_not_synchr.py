# Kerong Api. Редактирование соединения, без синхронизации

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import new_address_input_1, address_input_1, port_api_1
from test_func.func_search import search_line
from selenium.webdriver.common.keys import Keys
from time import sleep
from termcolor import cprint

def edit_kerong_not_synchr(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Kerong Api. Редактирование соединения, без синхронизации / test_func_edit_kerong_api_not_synchr", "yellow")

    # клик на настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Настройки']"))).click()

    # клик по разделу kerong api
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class  = 'settings-item'])[2]"))).click()

    # клик по кнопке Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Добавить']"))).click()

    # ввести адрес
    address = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id= 'Адрес']")))
    address.send_keys(Keys.BACKSPACE * 5)
    address.send_keys(address_input_1)
    sleep(0.2)
    print(f"IP первого соединения '{address_input_1}'")

    # ввести порт
    port = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id= 'Порт']")))
    port.send_keys(Keys.BACKSPACE * 5)
    port.send_keys(port_api_1)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class= 'UIbutton'])[4]"))).click()
    sleep(0.2)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    if search_line(browser, address_input_1):

        # открыть созданную карточку
        card = wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[contains(text(), '{address_input_1}')]")))
        card.click()
        sleep(0.1)

        # редактировать ip
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Редактировать']"))).click()
        ip_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Адрес']")))
        sleep(0.1)
        ip_input.send_keys(Keys.BACKSPACE * 20)
        sleep(0.1)
        ip_input.send_keys(new_address_input_1)
        sleep(0.1)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
        sleep(0.1)
        print(f"IP первого соединения изменен '{new_address_input_1}'")

    else:
        print(f"{new_address_input_1} - не найден")

    # Проверка наличия созданной карточки
    if search_line(browser, new_address_input_1):
        print()
    else:
        print(f"'{new_address_input_1}' - не найден")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
 #               pytest.fail()

def test_edit_kerong_not_synchr(browser):
    edit_kerong_not_synchr(browser)






