# Тип идентификатора. Создание карточки

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_func.func_search import search_line
from time import sleep
from termcolor import cprint
from config import name_type_identif



def add_type_ident(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Тип идентификатора. Создание карточки / test_func_add_type_identif", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Типы идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[4]"))).click()

    # Клик по кнопке Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Добавить']"))).click()

    # Ввести наименование
    name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Наименование']")))
    name.send_keys(name_type_identif)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(1)
    print(f"Создан тип идентификатора со значением '{name_type_identif}'")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")
        print()

    # проверка наличия созданной карточки
    if search_line(browser, name_type_identif):
        print()
    else:
        print(f"'{name_type_identif}' - не найден")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
#                pytest.fail()

def test_add_type_ident(browser):
    add_type_ident(browser)