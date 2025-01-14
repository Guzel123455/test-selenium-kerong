# Идентификатор. Создание карточки

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_func.func_search import search_line
from time import sleep
from termcolor import cprint
from config import name_type_identif, name_identif
import random

def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.5)

def add_ident(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Идентификатор. Создание карточки / test_func_add_identif", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[5]"))).click()

    # Клик по кнопке Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Добавить']"))).click()

    # Выбрать тип идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать тип идентификатора']"))).click()

    # список доступных ТИ
    identificators = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))
    # извлекаем текст из ТИ
    identificator_texts = [item.text for item in identificators]

    # Выбираем случайный идентификатор
    selected_type_identif = random.choice(identificator_texts)

    # Прокручиваем до нужного элемента типа идентификатора
    option_to_select = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text()= '{selected_type_identif}']")))
    scroll_to_element(browser, option_to_select)  # Прокручиваем к выбранному элементу
    sleep(0.1)
    option_to_select.click()

    # Ввести значение
    name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Значение']")))
    name.send_keys(name_identif)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(1)
    print(f"Создан идентификатор со значением '{name_identif}'")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")


    # проверка наличия созданной карточки
    if search_line(browser, name_identif):
        print()
    else:
        print(f"{name_identif} - не найден.")

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")


def test_add_ident(browser):
    add_ident(browser)