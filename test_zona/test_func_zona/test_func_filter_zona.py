# Зоны. Фильтр

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

def filter_zona(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Зоны. Фильтр / test_func_filter_zona", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()
    sleep(0.1)

    # Клик на Зоны
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[1]"))).click()

    # клик на кнопку Фильтр
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "filter-button"))).click()
    sleep(0.1)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать режим доступа']"))).click()
    sleep(0.1)

    # выбрать режим доступа Публичный
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Публичный']"))).click()
    sleep(0.1)

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Применить']"))).click()

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

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
                if h2_text1 == 'Публичный':
                    print(f"'{h2_text1}' - данный режим доступа найден")
                    found = True
                    break
            except Exception:
                continue
        if not found:
            print(f"{h2_text1} - значение не найдено")
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
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать режим доступа']"))).click()
    sleep(0.1)

    # выбрать режим доступа Приватный
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Приватный']"))).click()
    sleep(0.1)

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Применить']"))).click()
    sleep(0.5)

    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

        found = False
        for row in rows:
            try:
                h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
                h2_text2 = h2_element.text.strip()

                if h2_text2 == 'Приватный':
                    print(f"{h2_text2} - данный режим доступа найден")
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
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать режим доступа']"))).click()
    sleep(0.1)

    # выбрать режим доступа Корпоративный
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='Корпоративный']"))).click()
    sleep(0.1)

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Применить']"))).click()

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    sleep(0.5)

    # проверка найденного результата
    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        found = False
        for row in rows:
            try:
                h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
                h2_text3 = h2_element.text.strip()
                if h2_text3 == 'Корпоративный':
                    print(f"{h2_text3} - данный режим доступа найден")
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

def test_filter_zona(browser):
    filter_zona(browser)







