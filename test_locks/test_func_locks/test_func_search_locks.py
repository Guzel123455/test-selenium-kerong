# Замки и ячейки. Строка Поиска

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
from termcolor import cprint


def click_empty_space(browser):
    actions = ActionChains(browser)
    actions.move_by_offset(0, 0).click().perform()

def search_locks(browser):
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 10)

    cprint("Замки и ячейки. Строка Поиска / test_func_search_locks", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Замки и ячейки
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[3]"))).click()
    sleep(0.1)


    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

    if rows:
        # Получаем наименование первого набора замков
        first_lock_set_name = rows[0].find_element(By.CSS_SELECTOR, "td:nth-child(1) h2").text

        # строка поиска
        search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Поиск']")))
        search.send_keys(first_lock_set_name)
        print(f"Поиск по значению '{first_lock_set_name}'")
        sleep(1)

        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
            h2_text = h2_element.text.strip()

            if h2_text == first_lock_set_name:
                print(f"'{h2_text}' найден")
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(0.3)
                return True
            else:
                print(f"Значение не найдено")
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(0.1)

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

def test_search_locks(browser):
    search_locks(browser)




