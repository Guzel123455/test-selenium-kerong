# Клиенты. Фильтр по полу -  женский пол

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
from time import sleep


def filter_female(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Фильтр по полу -  женский пол / test_func_filter_female", "yellow")

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # клик по фильтру
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()

    # клик на Пол
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Пол']"))).click()

    # снять галочку с М.пол
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h4[text()= 'Мужской']"))).click()

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Применить']"))).click()
    sleep(2)

    rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    female_count = 0

    for row in rows:
        h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(4) h2")
        h2_text = h2_element.text
        if h2_text == "Ж":
            female_count += 1

    if female_count > 0:
        female_element = browser.find_element(By.CSS_SELECTOR, "p.MuiTablePagination-displayedRows.css-1chpzqh")
        female_element_text = female_element.text
        print(f"Количество отфильтрованных клиентов (Ж): {female_element_text}")
    else:
        print("Не найдено клиентов женского пола")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    # клик по фильтру
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()
    # сброс фильтра
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Сбросить']"))).click()
    sleep(0.2)

def test_filter_female(browser):
    filter_female(browser)