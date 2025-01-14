# Зоны. Создание корпоративной зоны

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_func.func_search import search_line
from selenium.webdriver import Keys
from time import sleep
from termcolor import cprint
from config import name_zone_corp, num_to_corp, num_from_corp



def add_zone_corp(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Зоны. Создание корпоративной зоны / test_func_add_zone_corp", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик на Зоны
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[1]"))).click()

    # Клик на Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'UIbutton']"))).click()

    # Ввести наименование
    name_zone = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Название зоны']")))
    name_zone.send_keys(name_zone_corp)

    # Номера От
    num1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Номера от']")))
    num1.send_keys(Keys.CONTROL, "a")
    num1.send_keys(num_from_corp)

    # Номера До
    num2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'до']")))
    num2.send_keys(Keys.CONTROL, "a")
    num2.send_keys(num_to_corp)

    # Режим доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Режим доступа']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Корпоративный']"))).click()

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(1)
    print(f"Зона '{name_zone_corp}' создана")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текс уведомления: {last_notification_text}")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
 #               pytest.fail()

    # проверка наличия созданной карточки
    if search_line(browser, name_zone_corp):
        print()
    else:
        print(f"{name_zone_corp} - не найден.")

# Выполнение функции
def test_add_zone_corp(browser):
    add_zone_corp(browser)




