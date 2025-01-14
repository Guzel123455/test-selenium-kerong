# Идентификаторы. Фильтр

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, ElementClickInterceptedException
from termcolor import cprint
from time import sleep


def scroll_to_element(browser, element):
    browser.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
    sleep(0.3)

def click_element(browser, locator):
    try:
        button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(locator))
        button.click()
    except ElementClickInterceptedException:
        browser.execute_script("arguments[0].click();", button)

def filter_identif(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Идентификаторы. Фильтр / test_func_filter_identif", "yellow")

    # Клик на Справочники
    click_element(browser, (By.XPATH, "//button[text()='Справочники']"))

    # Клик по идентиф
    click_element(browser, (By.XPATH, "(//div[@class='table-item'])[5]"))

    # первый в списке
    first_row_value = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tbody tr:first-child td:nth-child(2) h2"))).text
    print(f"Выбрано значение '{first_row_value}'")

    # клик на кнопку Фильтр
    click_element(browser, (By.CLASS_NAME, "filter-button"))

    # Вход в выпадающий список и его открытие
    click_element(browser, (By.XPATH, "//div[@id='Выбрать']"))

    # выбрать ТИ
    button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[text()= '{first_row_value}']")))
    scroll_to_element(browser, button)
    click_element(browser, (By.XPATH, f"//li[text()= '{first_row_value}']"))

    # Применить
    click_element(browser, (By.XPATH, "//button[text() = 'Применить']"))
    sleep(0.2)

    # проверка найденного результата
    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

        found_values = []  # Список для хранения найденных значений
        for row in rows:
            try:
                h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
                h2_text = h2_element.text.strip()
                if h2_text == first_row_value:
                    first_column_value = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2").text.strip()
                    found_values.append(first_column_value)  # Сохраняем найденное значение
            except Exception:
                continue
        # Вывод значений всех найденных элементов
        if found_values:
            print("Найденные значения у данного Типа идентификатора:")
            for value in found_values:
                print(value)
        else:
            print(f"{first_row_value} - значение не найдено")

    except TimeoutException:
        print("Нет значений")

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

def test_filter_identif(browser):
    filter_identif(browser)
