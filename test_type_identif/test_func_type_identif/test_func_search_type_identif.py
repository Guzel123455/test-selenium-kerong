# Типы идентификаторов. Строка Поиска

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from termcolor import cprint


def click_empty_space(browser):
    actions = ActionChains(browser)
    actions.move_by_offset(0, 0).click().perform()

def search_type_identif(browser):
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 10)

    cprint("Типы идентификаторов. Строка Поиска / test_func_search_type_identif", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Типы идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[4]"))).click()

    # данные первого ТИ в списке
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    type = browser.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
    type_txt = type.text

    # строка поиска
    search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Поиск']")))
    search.send_keys(type_txt)
    sleep(1)
    print(f"Поиск по значению '{type_txt}'")

    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    for row in rows:
        h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
        h2_text = h2_element.text.strip()

        if h2_text == type_txt:
            print(f"'{h2_text}' найден")
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            return True
        else:
            print(f"Значение не найдено")
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            #time.sleep(0.1)

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

def test_search_type_identif(browser):
    search_type_identif(browser)





