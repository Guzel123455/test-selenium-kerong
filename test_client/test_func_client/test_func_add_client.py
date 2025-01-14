# Клиенты. Создать карточку клиента

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
from faker import Faker
from datetime import datetime, timedelta
from termcolor import cprint


def add_client(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Создать карточку клиента / test_func_add_client", "yellow")

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # клик Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить']"))).click()

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
    client_num = ''.join(['9'] + [str(random.randint(0, 9)) for _ in range(8)])
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
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='UIbutton'])[2]"))).click()
    sleep(1)

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    # нажать кнопку назад
    button_back = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='back-to']")))
    button_back.click()
    sleep(0.1)

    # Проверка наличия клиента
    if search_client(browser, client_num):
        print()
    else:
        print(f"{client_num} - не найден.")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")


def search_client(browser, client_num):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

    # Убираем "+7" из номера для корректного поиска
    clean_client_num = client_num.replace("+7", "")

    for row in rows:
        phone = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2").text.strip()
        # Убираем "+7" и проверяем только номера
        clean_phone = phone.replace("+7", "").replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        if clean_phone.endswith(clean_client_num):  # Сравниваем последние 10 символов
            print(f"Найден клиент с номером '{client_num}'")
            return True

    # Переход на следующую страницу
    try:
        next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
        next_page.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr")))
        return search_client(browser, client_num)
    except Exception:
        print("Не найден на всех страницах")
        return False




def test_add_client(browser):
    add_client(browser)
