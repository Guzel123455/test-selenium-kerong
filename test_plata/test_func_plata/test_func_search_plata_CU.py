# Платы. Строка Поиска. СU платы

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from termcolor import cprint
from selenium.webdriver.common.keys import Keys
from time import sleep


def click_empty_space(browser):
    actions = ActionChains(browser)
    actions.move_by_offset(0, 0).click().perform()

def search_plata_CU(browser):
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 10)

    cprint("Платы. Строка Поиска. СU платы / test_func_search_plata_CU", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[2]"))).click()
    sleep(0.1)

    # Клик на CU-Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h4[text() = 'CU - платы']"))).click()
    sleep(2)

    # данные первой строки в списке
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))

    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    if rows:

        name = rows[0].find_element(By.CSS_SELECTOR, "td:nth-child(1) h2").text

        # строка поиска
        search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Поиск']")))
        search.send_keys(name)
        sleep(1)
        print(f"Поиск по значению '{name}'")

        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
            h2_text = h2_element.text.strip()

            if h2_text == name:
                print(f"'{h2_text}' найден")
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                return True
            else:
                print(f"Значение не найдено")
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(
                    f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

def test_search_plata_CU(browser):
    search_plata_CU(browser)





