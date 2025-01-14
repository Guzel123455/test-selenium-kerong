# Платы. Создание платы CU
from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_func.func_search import search_line
from time import sleep
from termcolor import cprint
from config import number_in_chain, name_CU_text, name_BU_text


def add_card_CU(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Платы. Создание платы CU / test_func_add_plata_CU", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class ='table-item'])[2]"))).click()

    # Добавить KR-CU
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить KR-CU']"))).click()

    # Ввести наименование
    name_plata = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Наименование платы']")))
    name_plata.send_keys(name_CU_text)

    # Выбрать тип KR-CU
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать тип KR-CU']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='CU_48']"))).click()

    # Выбрать плату KR-BU
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='Выбрать плату KR-BU']"))).click()
    bu = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text()= '{name_BU_text}']")))
    browser.execute_script("arguments[0].scrollIntoView();", bu)
    sleep(0.1)
    bu.click()

    # Номер в цепи
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='Номер в цепи']"))).click()
    num = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text()= '{number_in_chain}']")))
    browser.execute_script("arguments[0].scrollIntoView();", num)
    sleep(0.1)
    num.click()

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(0.2)
    print(f"Плата '{name_CU_text}' создана")

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

    # открыть вкладку CU платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h4[text() = 'CU - платы']"))).click()
    sleep(0.1)

    # проверка наличия созданной карточки
    if search_line(browser, name_CU_text):
        print()
    else:
        print(f"'{name_CU_text}' - не найден.")


    # Выполнение функции
def test_add_card_CU(browser):
    add_card_CU(browser)