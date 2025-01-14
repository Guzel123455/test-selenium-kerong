# Клиенты. Карточка клиента. Снять активность

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_client.test_func_client.func_search_client import search_phone
from time import sleep
from termcolor import cprint

def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)

def deactivating_client(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Карточка клиента. Снять активность / test_func_deactivating_client", "yellow")

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # данные первого клиента в списке
    client = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'amount-sublime-container']")))
    name = browser.find_element(By.CSS_SELECTOR, "td:nth-child(1) h4")
    name_txt = name.text
    mobile = browser.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
    mobile_txt = mobile.text
    client.click()
    print(f"Снять активность клиенту '{name_txt}', '{mobile_txt}'")

    # снять активность
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Снять активность']"))).click()
    sleep(0.5)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    # нажать кнопку назад
    button_back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='back-to']")))
    button_back.click()
    sleep(0.1)
    #
    # # проверка наличия карточки
    # if search_phone(browser, mobile_txt):
    #     print()
    # else:
    #     print(f"'{mobile_txt}' - не найден")
    #

def test_deactivating_client(browser):
    deactivating_client(browser)