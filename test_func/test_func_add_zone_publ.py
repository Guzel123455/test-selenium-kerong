# добавление зоны и проверка наличия карточки

import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_func.func_search import scroll_to_element, search_line
from config import name_zone_text, num_from, num_to
from browser_setup import browser


def create_and_zone(browser):
    wait = WebDriverWait(browser, 20)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик на Зоны
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[1]"))).click()

    # Клик на Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'UIbutton']"))).click()

    # Ввести наименование
    name_zone = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name_zone.send_keys(name_zone_text)

    # Колво замков
    count_keys = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[3]")))
    count_keys.send_keys(Keys.CONTROL, "a")
    count_keys.send_keys("48")

    # Номера От
    num1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[4]")))
    num1.send_keys(Keys.CONTROL, "a")
    num1.send_keys(num_from)

    # Номера До
    num2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[5]")))
    num2.send_keys(Keys.CONTROL, "a")
    num2.send_keys(num_to)

    # Режим доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'demo-simple-select-helper']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Публичный']"))).click()

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    time.sleep(1)
    print("Зона создана")

    # проверка наличия созданной карточки
    if search_line(browser, name_zone_text):
        print(f"{name_zone_text} - найден")
        print()
    else:
        print(f"{name_zone_text} - не найден.")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(
                    f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                pytest.fail()

# Выполнение функции
def test_create_and_zone(browser):
    create_and_zone(browser)




