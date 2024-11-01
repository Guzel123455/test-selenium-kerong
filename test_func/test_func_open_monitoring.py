# Мониторинг. Открыть зону, получить список замков

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import name_zone_publ
from browser_setup import browser

def open_monitor(browser):
    wait = WebDriverWait(browser, 20)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # открыть зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[contains(text(), '{name_zone_publ}')]"))).click()

    # количество ячеек
    cells = browser.find_elements(By.CLASS_NAME, 'lock-item-container')
    cell_count = len(cells)
    print(f'Количество ячеек: {cell_count}')

    if cell_count > 0:
        first_num = cells[0].find_element(By.CLASS_NAME, 'title').text
        last_num = cells[-1].find_element(By.CLASS_NAME, 'title').text
        print(f'Первая: {first_num}')
        print(f'Последняя: {last_num}')
        return first_num

    # клик назад
    browser.find_element(By.CLASS_NAME, 'back-to').click()
    time.sleep(0.1)

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
#                pytest.fail()

def test_open_monitor(browser):
    open_monitor(browser)

