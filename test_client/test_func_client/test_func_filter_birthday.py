# Клиенты. Фильтр по дате рождения

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
from datetime import datetime
from time import sleep
import random


def filter_birthday(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Фильтр по дате рождения / test_func_filter_birthday", "yellow")

    # Клик по кнопке Клиенты
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Клиенты']"))).click()
    sleep(0.2)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr")))

    # собираю все даты на первой странице
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    birthdays = []
    for row in rows:
        try:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(5) h2")
            h2_text = h2_element.text.strip()
            if h2_text and h2_text.lower() != 'не указана':
                birthdays.append(h2_text)
        except Exception as e:
            break

    # фильтр дат по возрастанию
    birthdays.sort(key=lambda date: datetime.strptime(date, '%d.%m.%Y'))

    # первая дата рождения
    start_date = birthdays[0]
    # вторая дата, на 1 строку ниже в отфильтрованном списке
    end_date = birthdays[1]

    print(f"Начальная дата - {start_date}, Конечная дата - {end_date}")

    # Клик по фильтру
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='filter-button']"))).click()

    # Клик на Дата рождения
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Дата рождения']"))).click()

    # Ввести стартовую дату рождения
    start_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder= 'DD.MM.YYYY']")))
    start_input.click()
    start_input.send_keys(start_date)

    # Ввести конечную дату рождения
    stop_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder= 'DD.MM.YYYY'])[2]")))
    stop_input.click()
    stop_input.send_keys(end_date)

    # Применить фильтр
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Применить']"))).click()

    # Проверка отфильтрованных дат
    filtered_birthdays = []
    rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    for row in rows:
        try:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(5) h2")
            h2_text = h2_element.text

            if h2_text and h2_text.lower() != 'не указана':
                filtered_birthdays.append(h2_text)
        except Exception as e:
            print(f"Ошибка при получении даты рождения: {e}")

    if all(is_date_in_range(b, start_date, end_date) for b in filtered_birthdays):
        print("Найденные даты после применения фильтра:")
        for date in filtered_birthdays:
            print(date)
    else:
        print("Нет клиентов в данном диапазоне дат рождения")


    displayed_dates = [row.find_element(By.CSS_SELECTOR, "td:nth-child(5) h2").text.strip() for row in rows if row.find_elements(By.CSS_SELECTOR, "td:nth-child(5) h2")]

    # проверка начальной и конечной даты
    if start_date in displayed_dates and end_date in displayed_dates:
        print(f"Начальная дата {start_date} и конечная дата {end_date} отображаются")
    else:
        if start_date not in displayed_dates:
            print(f"Начальная дата {start_date} не отображается")
        if end_date not in displayed_dates:
            print(f"Конечная дата {end_date} не отображается")


    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    # клик по фильтру
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()
    # сброс фильтра
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Сбросить']"))).click()

# проверка, находится ли дата в заданном диапозоне
def is_date_in_range(date_str, start_date, end_date):
    date = datetime.strptime(date_str, '%d.%m.%Y')
    start = datetime.strptime(start_date, '%d.%m.%Y')
    end = datetime.strptime(end_date, '%d.%m.%Y')
    return start <= date <= end

def test_filter_birthday(browser):
    filter_birthday(browser)