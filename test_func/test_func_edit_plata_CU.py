# редактирование карточки BU и проверка наличия карточки

import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import name_CU_text, new_name_CU_text
from browser_setup import browser

def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.1)

def edit_card_CU(browser):
    wait = WebDriverWait(browser, 10)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()
    time.sleep(0.1)

    # Клик на Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[2]"))).click()
    time.sleep(0.1)

    # Клик на CU-Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h4[text() = 'CU - платы']"))).click()
    time.sleep(0.1)

    def search_plata_CU(browser):
        # поиск карточки платы
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
            h2_text = h2_element.text

            # Прокрутка к элементу
            scroll_to_element(browser, h2_element)

            if h2_text == name_CU_text:
                # открыть плату с наименование name_BU_text
                browser.find_element(By.XPATH, f"//h2[text()= '{name_CU_text}']").click()

                # редактировать
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Редактировать']"))).click()

                # изменить наименование
                text_name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
                text_name.send_keys(Keys.BACKSPACE * 30)
                text_name.send_keys(new_name_CU_text)

                # номер в цепи
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='demo-simple-select-helper'])[2]"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='1']"))).click()

                # сохранить
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
                time.sleep(0.1)
                return True

        # если карточка не найдена, след старница
        try:
            next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
            next_page.click()
            time.sleep(0.1)
            return search_plata_CU(browser)
        except:
            print("Не найден на всех страницах.")
            return False

    # проверка наличия отредактированой карточки
    if search_plata_CU(browser):
        print(f"{new_name_CU_text} - отредактирована")
    else:
        print(f"{new_name_CU_text} - не найдена")

    # проверка статус кодов, при статусе кроме 200 и 101 тест падает
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                pytest.fail()

# Выполнение функции
def test_edit_card_CU(browser):
    edit_card_CU(browser)

