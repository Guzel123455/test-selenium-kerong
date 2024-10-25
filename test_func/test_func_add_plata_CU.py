# добавление CU и проверка наличия карточки

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import name_CU_text, name_BU_text, number_in_chain
from browser_setup import browser
from test_func.func_search import scroll_to_element, search_line


def create_and_check_card_CU(browser):
    wait = WebDriverWait(browser, 20)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class ='table-item'])[2]"))).click()

    # Добавить KR-CU
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить KR-CU']"))).click()

    # Ввести наименование
    name_plata = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name_plata.send_keys(name_CU_text)

    # Выбрать тип KR-CU
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'demo-simple-select-helper'])[1]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='CU_48']"))).click()

    # Выбрать плату KR-BU
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='demo-simple-select-helper'])[2]"))).click()
    bu = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text()= '{name_BU_text}']")))
    browser.execute_script("arguments[0].scrollIntoView();", bu)
    time.sleep(0.1)
    bu.click()

    # Номер в цепи
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='demo-simple-select-helper'])[3]"))).click()
    num = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text()= '{number_in_chain}']")))
    browser.execute_script("arguments[0].scrollIntoView();", num)
    time.sleep(0.1)
    num.click()

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    time.sleep(0.2)
    print("Карточка CU создана")

    # открыть вкладку CU платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h4[text() = 'CU - платы']"))).click()
    time.sleep(0.1)

    # проверка наличия созданной карточки
    if search_line(browser, name_CU_text):
        print(f"{name_CU_text} - найден")
        print()
    else:
        print(f"{name_CU_text} - не найден.")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(
                    f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                pytest.fail()

    # Выполнение функции
def test_create_and_check_card_CU(browser):
    create_and_check_card_CU(browser)