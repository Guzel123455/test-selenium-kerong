# Kerong Api. Строка Поиска

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from termcolor import cprint
from selenium.webdriver import Keys
from time import sleep


def search_kerong(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    cprint("Kerong Api. Строка Поиска / test_func_search_kerong_api", "yellow")

    # клик на настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Настройки']"))).click()

    # клик по разделу kerong api
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class  = 'settings-item'])[2]"))).click()

    # клик по строке поиска и ввод значения
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    if rows:
        name = rows[0].find_element(By.CSS_SELECTOR, "td:nth-child(1) h2").text

        # строка поиска
        search = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type = 'search']")))
        search.send_keys(name)
        print(f"Поиск по значению '{name}'")
        sleep(1)

        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
            h2_text = h2_element.text.strip()

            if h2_text == name:
                print(f"'{h2_text}' найден")
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(0.3)
                return True
            else:
                print("Значение не найдено")
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(0.1)


    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
#                pytest.fail()
                print()

def test_search_kerong(browser):
    search_kerong(browser)






