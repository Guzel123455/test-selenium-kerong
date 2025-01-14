# Клиенты. Карточка клиента. История операций аренды

from selenium.common import NoSuchElementException
from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from config import name_zone_private, num_from_private, num_to_private
from time import sleep
import random
from faker import Faker
from datetime import datetime, timedelta
from termcolor import cprint


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.5)

def choose_indent_in_client(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Карточка клиента. История операций аренды / test_func_client_history_operations", "yellow")

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
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='Выбрать пол']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[text()='{gender}']"))).click()

    # ввести дату рождения
    def random_date(start, end):
        return start + timedelta(days=random.randint(0, (end - start).days))

    # диапазон дат
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2024, 12, 31)

    # Генерирация даты
    random_birthday = random_date(start_date, end_date).strftime('%d%m%Y')
    birthday = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2']")))
    birthday.click()
    birthday.send_keys(random_birthday)

    print(f"Создан клиент- {client_lastname} {client_firstname}, телефон- {client_num}, дата рождения- {random_birthday}")

    # сохранить
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@class='UIbutton'])[2]"))).click()

    # Кнопка "Выбрать"
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Выбрать']"))).click()
    sleep(0.2)

    # Клик по идентификатору
    ident = browser.find_element(By.CSS_SELECTOR, "tbody tr:first-child h2")
    print(f"Клиенту '{client_lastname}' привязан идентификатор '{ident.text}'")
    ident.click()
    sleep(0.2)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

def client_history_operation(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    # открыть вкладку Доступ к ячейкам
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Доступ к ячейкам']"))).click()

    # добавить доступ
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Добавить доступ']"))).click()

    # Выбрать тип аренды
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id = 'Выбрать тип аренды ']"))).click()

    # по идентификатору
    wait.until(EC.visibility_of_element_located((By.XPATH, "//li[text() = 'По идентификатору']"))).click()

    # выбрать идентификатор
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id = 'Выбрать идентификатор']"))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul:nth-child(1) li"))).click()

    # выбрать зону
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id = 'Выбрать зону']"))).click()
    zona = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text() = '{name_zone_private} [{num_from_private} - {num_to_private}]']")))
    browser.execute_script("arguments[0].scrollIntoView(true);", zona)
    wait.until(EC.element_to_be_clickable(zona)).click()

    # Случайный номер ячейки из диапазона
    random_cell_number = random.randint(int(num_from_private), int(num_to_private))
    # ввести номер ячейки
    num = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id = 'Введите номер ячейки']")))
    num.send_keys(str(random_cell_number))

    # Начало периода
    start_date = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw']")))
    start_date.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class = 'MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()

    # Конец периода
    end_date = wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw'])[2]")))
    end_date.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class = 'MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()

    # начальное время
    input_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[2]")))
    input_element.click()
    input_value = input_element.get_attribute("value")
    hours, minutes = map(int, input_value.split(':'))

    # +1 час от начального времени
    hours += 1
    if hours == 24:
        hours = 0
    new_time = f"{hours:02}:{minutes:02}"

    # конечное время
    time_end = wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[4]")))
    time_end.click()
    time_end.send_keys(new_time)
    sleep(0.1)

    # сохранить
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Сохранить']"))).click()

    # Получение текущей даты и времени
    current_datetime = datetime.now().strftime("%d.%m.%Y")
    print(f"Создана аренда на ячейку '{random_cell_number}', на {current_datetime} с {input_value} по {new_time}")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    # удалить
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "svg > path[d='M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6zM19 4h-3.5l-1-1h-5l-1 1H5v2h14z']"))).click()
    sleep(0.2)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    # история аренд
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text() = 'История аренд']"))).click()
    sleep(2)

    # аренда созданная в клиенте
    rent_start = f"{current_datetime} | {input_value}"
    rent_end = f"{current_datetime} | {new_time}"

    # все строки в истории аренды
    rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr")))

    # Флаг, который будет указывать, найдена ли дата начала аренды
    start_found = False

    # Проходим по каждой строке
    for index, row in enumerate(rows):
        # Получаем первую ячейку с датой и временем начала периода
        try:
            # дата начала
            start_period = row.find_element(By.XPATH, ".//td[3]/h2").text.strip()
            stop_period = row.find_element(By.XPATH, ".//td[4]/h2").text.strip()

            # Поиск совпадений
            if start_period == rent_start:
                start_found = True
                if stop_period == rent_end:
                    print(f"Созданная аренда найдена на строке {index + 1}: {start_period}")
                    actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                    break
                else:
                    raise AssertionError("Дата окончания аренды не соответствует")

        except NoSuchElementException:
            continue  # Пропустить текущую строку, если она не содержит нужных данных

        # Если дата начала не была найдена
    if not start_found:
        raise AssertionError("Нет данных с заданным временем и датой")


def test_choose_indent_in_client(browser):
    choose_indent_in_client(browser)
    return choose_indent_in_client(browser)

def test_client_history_operation(browser):
    client_history_operation(browser)

