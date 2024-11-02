# добавление клиента и проверка наличия

import time
import random
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from test_func.func_search_client import search_phone
from browser_setup import browser

def add_client(browser):
    wait = WebDriverWait(browser, 10)
    browser.get("http://192.168.25.137")

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # клик Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить']"))).click()
    time.sleep(0.1)

    # ввести фамилию
    enter_lastname = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='outlined-basic']")))
    enter_lastname.click()
    fake = Faker("ru_RU")

    # фамилию в переменную
    client_lastname = fake.last_name_male()
    enter_lastname.send_keys(client_lastname)
    print(client_lastname)

    # ввести имя
    enter_firstname = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@id='outlined-basic'])[2]")))
    enter_firstname.click()
    fake = Faker("ru_RU")

    # имя в переменную
    client_firstname = fake.first_name_male()
    enter_firstname.send_keys(client_firstname)
    print(client_firstname)

    # ввести номер телефона
    enter_phone = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='tel']")))
    client_number = '9' + ''.join([str(random.randint(0, 9)) for _ in range(9)])
    client_num = "+7" + ''.join(client_number)
    enter_phone.send_keys(client_num)
    print(client_num)

    # ввести дату рождения
    def random_date(start, end):
        return start + timedelta(days=random.randint(0, (end - start).days))

    # диапазон дат
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2024, 12, 31)

    # Генерирация даты
    random_birthday = random_date(start_date, end_date).strftime('%d%m%Y')
    birthday = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2']")))
    birthday.click()
    birthday.send_keys(random_birthday)
    print(random_birthday)

    # сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='UIbutton'])[2]"))).click()
    time.sleep(0.5)

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
 #               pytest.fail()

    # нажать кнопку назад
    button_back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='back-to']")))
    button_back.click()
    time.sleep(0.1)

    # проверка наличия созданной карточки
    if search_phone(browser, client_num):
        print(f"{client_num} - найден")
        print()
    else:
        print(f"{client_num} - не найден.")


