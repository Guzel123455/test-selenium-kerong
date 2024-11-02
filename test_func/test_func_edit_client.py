# редактирование карточки клиента

import time
import random
from faker import Faker
from test_func.func_search_client import search_phone
from browser_setup import browser
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def edit_client(browser):
    wait = WebDriverWait(browser, 10)

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # данные первого клиента в списке
    client = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'amount-sublime-container']")))
    name = browser.find_element(By.CSS_SELECTOR, "td:nth-child(1) h4")
    name_txt = name.text
    print(name_txt)
    mobile = browser.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
    mobile_txt = mobile.text
    print(mobile_txt)
    client.click()

    # редактировать
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Редактировать']"))).click()

    # изменить имя
    name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name.click()
    name.send_keys(Keys.BACKSPACE * 30)
    fake = Faker("ru_RU")
    new_name = fake.first_name_male()
    name.send_keys(new_name)
    print(f"Новое имя '{new_name}'")

    # изменить номер телефона
    enter_phone = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='tel']")))
    enter_phone.click()
    enter_phone.send_keys(Keys.BACKSPACE * 30)
    client_number = '9' + ''.join([str(random.randint(0, 9)) for _ in range(9)])
    client_num = "+7" + ''.join(client_number)
    enter_phone.send_keys(client_num)
    print(f"Новый номер '{client_num}'")

    # сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='UIbutton'])[2]"))).click()
    time.sleep(1)

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    # нажать кнопку назад
    button_back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='back-to']")))
    button_back.click()
    time.sleep(0.1)

    # проверка наличия созданной карточки
    if search_phone(browser, client_num):
        print()
    else:
        print(f"'{client_num}' - не найден")


def test_edit_client(browser):
    edit_client(browser)