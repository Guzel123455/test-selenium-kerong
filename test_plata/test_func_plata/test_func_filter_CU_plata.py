# Платы. Фильтры в CU платах

from browser_setup import browser
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
from time import sleep


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.1)

def filter_CU_plata(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Платы. Фильтры в CU платах / test_func_filter_CU_plata", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()
    sleep(0.1)

    # Клик на Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[2]"))).click()
    sleep(0.1)

    # Клик на CU-Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h4[text() = 'CU - платы']"))).click()
    sleep(0.1)

    # клик на кнопку Фильтр
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "filter-button"))).click()
    sleep(0.1)

    # выбрать тип платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать']"))).click()
    sleep(0.1)
    # cu-48
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='CU-48']"))).click()
    sleep(0.1)

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Применить']"))).click()
    sleep(0.5)

    # проверка найденного результата
    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

        found = False
        for row in rows:
            try:
                h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
                h2_text1 = h2_element.text.strip()
                if h2_text1 == 'CU-48':
                    print(f"'{h2_text1}' - данный тип платы найден")
                    found = True
                    break
            except Exception:
                continue
        if not found:
            print(f"'{h2_text1}' - значение не найдено")
    except TimeoutException:
        print("Нет значений")

    # клик на кнопку Фильтр
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "filter-button"))).click()
    sleep(0.1)

    # сброс данных
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Сбросить']"))).click()
    sleep(0.1)

    # клик на кнопку Фильтр
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "filter-button"))).click()
    sleep(0.1)

    # номер в цепи
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'Выбрать'])[2]"))).click()
    sleep(0.1)

    # выбрать номер в цепи
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='0']"))).click()
    sleep(0.1)

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Применить']"))).click()
    sleep(0.5)

    # проверка найденного результата
    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

        found = False
        for row in rows:
            try:
                h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(3) h2")
                h2_text2 = h2_element.text.strip()
                if h2_text2 == '0':
                    print(f"'{h2_text2}' - данный тип платы найден")
                    found = True
                    break
            except Exception:
                continue
        if not found:
            print(f"'{h2_text2}' - значение не найдено")
    except TimeoutException:
        print("Нет значений")

    # клик на кнопку Фильтр
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "filter-button"))).click()
    sleep(0.1)

    # сброс данных
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Сбросить']"))).click()
    sleep(0.1)

    # клик на кнопку Фильтр
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "filter-button"))).click()
    sleep(0.1)

    # BU-плата
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'Выбрать'])[3]"))).click()
    sleep(0.1)

    # выбрать плату
    name_plata = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul/li[1]")))
    plata_name = name_plata.text
    name_plata.click()
    sleep(0.1)

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Применить']"))).click()
    sleep(0.5)

    # проверка найденного результата
    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        found = False
        for row in rows:
            try:
                h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(4) h2")
                h2_text3 = h2_element.text.strip()
                if h2_text3 == plata_name:
                    print(f"'{h2_text3}' - данный тип платы найден")
                    found = True
                    break
            except Exception:
                continue
        if not found:
            print(f"'{h2_text3}' - значение не найдено")
    except TimeoutException:
        print("Нет значений")


    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

def test_filter_CU_plata(browser):
    filter_CU_plata(browser)






