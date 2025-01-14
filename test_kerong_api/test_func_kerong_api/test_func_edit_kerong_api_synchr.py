# Kerong Api. Редактирование соединения с синхронизацией

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from termcolor import cprint
from config import new_address_input_2, address_input_2, port_api_2
from test_func.func_search import search_line
from time import sleep
from selenium.webdriver.common.keys import Keys


def edit_kerong_synchr(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Kerong Api. Редактирование соединения с синхронизацией / test_func_edit_kerong_api_synchr", "yellow")

    # Клик на настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Настройки']"))).click()

    # Клик по разделу kerong api
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='settings-item'])[2]"))).click()

    # Клик по кнопке Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Добавить']"))).click()

    # Ввести адрес
    address = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id= 'Адрес']")))
    address.send_keys(Keys.BACKSPACE * 5)
    address.send_keys(address_input_2)
    print(f"IP второго соединения '{address_input_2}'")

    # Ввести порт
    port = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id= 'Порт']")))
    port.send_keys(Keys.BACKSPACE * 5)
    port.send_keys(port_api_2)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='UIbutton'])[4]"))).click()
    sleep(0.2)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    # Поиск созданной карточки на первой странице
    if search_line(browser, address_input_2):

        # Открыть созданную карточку
        card = wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[contains(text(), '{address_input_2}')]")))
        card.click()

         # Редактировать IP
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Редактировать']"))).click()
        ip_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Адрес']")))
        sleep(0.1)
        ip_input.send_keys(Keys.BACKSPACE * 20)
        sleep(0.1)
        ip_input.send_keys(new_address_input_2)
        sleep(0.1)
        print(f"IP второго соединения изменен '{new_address_input_2}'")

        # Использовать по умолчанию
        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='MuiSwitch-thumb css-19gndve']")))
        browser.execute_script("arguments[0].click();", checkbox)

        action = ActionChains(browser)
        for _ in range(3):
            action.click(checkbox)
        action.perform()

        # Сохранить
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='UIbutton'])[4]"))).click()
        sleep(0.2)

        # Проверка состояния карточки
        is_used = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Используется']")))
        is_used_text = is_used.text.strip()

        if is_used_text == "Используется":
            # Синхронизировать
            browser.find_element(By.XPATH, "(//button[@class='UIbutton'])[2]").click()
            print("Состояние Используется, Синхронизировано")
            sleep(2)

        else:
            # Строка с соединением
            wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[@class='MuiTableRow-root css-1axy92l']"))).click()

            # Кнопка редактировать
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='UIbutton'])[3]"))).click()

            # Использовать по умолчанию
            button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='MuiSwitch-thumb css-19gndve']")))
            browser.execute_script("arguments[0].click();", button)

            action = ActionChains(browser)
            for _ in range(2):
                action.click(button)
            action.perform()

            # Сохранить изменения
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
            sleep(0.1)
    else:
        print(f"{address_input_2} - не найден")

    # Проверка наличия созданной карточки
    if search_line(browser, new_address_input_2):
        print()
    else:
        print(f"{new_address_input_2} - не найден")


    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code}. Текст ошибки: {error_message}")
#                pytest.fail()
                print()


def test_edit_kerong_synchr(browser):
    edit_kerong_synchr(browser)
