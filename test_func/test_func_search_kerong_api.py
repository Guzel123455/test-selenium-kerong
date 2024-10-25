# авторизация и поиск керонг апи

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import address_input
from browser_setup import browser


def search_kerong(browser):
    wait = WebDriverWait(browser, 10)

    # клик на настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Настройки']"))).click()

    # клик по разделу kerong api
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class  = 'settings-item'])[2]"))).click()

    # клик по строке поиска и ввод значения
    search = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type = 'search']")))
    search.send_keys(address_input)
    time.sleep(0.1)

    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    total_found = len(rows)
    print(f"Total cards created: {total_found}")

    found = False
    for row in rows:
        h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
        h2_text = h2_element.text

        # Проверяем соответствие карточки искомому значению
        if h2_text == address_input:
            found = True

    # Вывод информации
    if found:
        print(f"Found IP: {address_input}")
    else:
        print(f"{address_input} - not found")

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(
                    f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                pytest.fail()

def test_search_kerong(browser):
    search_kerong(browser)






