# Клиенты. Добавить идентификатор в карточке Клиента

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from faker import Faker
from termcolor import cprint
from datetime import datetime, timedelta
import random


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.1)

def add_ident_in_client(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Добавить идентификатор в карточке Клиента / test_func_add_ident_in_client", "yellow")

    # клик по кнопке Клиент
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # клик Добавить
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Добавить']"))).click()

    # ввести фамилию
    enter_lastname = wait.until(EC.visibility_of_element_located((By.ID, "Фамилия")))
    enter_lastname.click()
    fake = Faker("ru_RU")
    client_lastname = fake.last_name_male()
    enter_lastname.send_keys(client_lastname)

    # ввести имя
    enter_firstname = wait.until(EC.visibility_of_element_located((By.ID, "Имя *")))
    enter_firstname.click()
    fake = Faker("ru_RU")
    client_firstname = fake.first_name_male()
    enter_firstname.send_keys(client_firstname)

    # ввести номер телефона
    enter_phone = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='tel']")))
    client_num = "+7" + ''.join(['9'] + [str(random.randint(0, 9)) for _ in range(8)])
    enter_phone.send_keys(client_num)

    # Случайный выбор пола
    gender = random.choice(["Мужской", "Женский"])

    # Выбрать пол
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='Выбрать пол']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[text()='{gender}']"))).click()

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

    print(f"Создан клиент- {client_lastname} {client_firstname}, телефон- {client_num}, дата рождения- {random_birthday}")

    # сохранить
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@class='UIbutton'])[2]"))).click()
    sleep(0.2)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    # Кнопка "Добавить"
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Добавить']"))).click()

    # имя клиента
    name = browser.find_element(By.XPATH, "//input[@id = 'Имя']")
    value = name.get_attribute("value")

    # Выбрать ТИ
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='Выбрать тип идентификатора']"))).click()
    sleep(0.1)
    # Клик по идентификатору
    type = browser.find_element(By.CSS_SELECTOR, "li:nth-child(1)")
    print(f"Выбран ТИ '{type.text}'")
    type.click()

    # ввести значение идентификатора
    ident = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id = 'Значение']")))
    ident.click()
    fake = Faker("ru_RU")
    ident_1 = fake.postcode()
    ident.send_keys(ident_1)
    print(f"Клиенту '{value}' привязан идентификатор '{ident_1}'")

    # сохранить
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Сохранить']"))).click()
    sleep(0.2)

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


def test_add_ident_in_client(browser):
    add_ident_in_client(browser)