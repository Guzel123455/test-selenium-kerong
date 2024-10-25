# добавление идентиф и проверка наличия карточки

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_func.func_search import scroll_to_element, search_line
from config import name_type_identif, name_identif
from browser_setup import browser

def create_ident(browser):
    wait = WebDriverWait(browser, 20)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Типы идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[5]"))).click()

    # Клик по кнопке Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Добавить']"))).click()

    # Выбрать тип идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'demo-simple-select-helper']"))).click()

    # Прокручиваем до нужного элемента типа идентификатора
    option_to_select = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text()= '{name_type_identif}']")))
    browser.execute_script("arguments[0].scrollIntoView();", option_to_select)
    time.sleep(0.5)
    option_to_select.click()

    # Ввести значение
    name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name.send_keys(name_identif)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    time.sleep(1)
    print(f"Карточка {name_identif} создана")


    # проверка наличия созданной карточки
    if search_line(browser, name_identif):
        print(f"{name_identif} - найден")
        print()
    else:
        print(f"{name_identif} - не найден.")

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(
                    f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                pytest.fail()

def test_create_ident(browser):
    create_ident(browser)