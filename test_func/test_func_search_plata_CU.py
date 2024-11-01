# Строка Поиск в разделе BU платы

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import new_edit_name_CU
from browser_setup import browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def click_empty_space(browser):
    actions = ActionChains(browser)
    actions.move_by_offset(0, 0).click().perform()

def search_plata_CU(browser):
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 20)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[2]"))).click()
    time.sleep(0.1)

    # Клик на CU-Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h4[text() = 'CU - платы']"))).click()
    time.sleep(0.3)

    # строка поиска
    searc = wait.until(EC.element_to_be_clickable((By.XPATH, "// input[@id = 'outlined-basic']")))
    searc.send_keys(new_edit_name_CU)
    print(f"Искомое значение '{new_edit_name_CU}'")
    time.sleep(1)

    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    for row in rows:
        h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
        h2_text = h2_element.text.strip()

        if h2_text == new_edit_name_CU:
            print(f"'{h2_text}' найден")
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            time.sleep(0.3)
            return True
        else:
            print(f"Значение не найдено")
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            time.sleep(0.1)

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

def test_search_plata_CU(browser):
    search_plata_CU(browser)





