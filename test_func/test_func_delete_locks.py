# удаление набора замков, первый в списке

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_func.func_search import search_line
from config import name_lock_text
from browser_setup import browser
from selenium.webdriver.common.action_chains import ActionChains

def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.1)

def delete_locks(browser):
    wait = WebDriverWait(browser, 20)
    actions = ActionChains(browser)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик на замки и ячейки
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'settings-item'])[3]"))).click()

    if search_line(browser, name_lock_text):
        print(f"{name_lock_text} - найден")
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='MuiBox-root css-0']"))).click()
        print(f"{name_lock_text} - удален")
        time.sleep(0.1)
        print()
    else:
        print(f"{name_lock_text} - не найден")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(
                    f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
#               pytest.fail()


def test_delete_locks(browser):
    delete_locks(browser)