# Клиенты. Редактирование карточки клиента

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
import random
from faker import Faker
from selenium.webdriver import Keys
from time import sleep


def edit_client(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Редактирование карточки клиента / test_func_edit_client", "yellow")

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # данные первого клиента в списке
    client = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'amount-sublime-container']")))
    name = browser.find_element(By.CSS_SELECTOR, "td:nth-child(1) h4")
    name_txt = name.text
    mobile = browser.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
    mobile_txt = mobile.text
    client.click()
    print(f"Выбран клиент- {name_txt}, телефон- {mobile_txt}")

    # редактировать
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Редактировать']"))).click()

    # изменить имя
    name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Имя']")))
    name.click()
    name.send_keys(Keys.BACKSPACE * 30)
    fake = Faker("ru_RU")
    new_name = fake.first_name_male()
    name.send_keys(new_name)

    # изменить номер телефона
    enter_phone = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='tel']")))
    enter_phone.click()
    enter_phone.send_keys(Keys.BACKSPACE * 30)
    client_number = '9' + ''.join([str(random.randint(0, 9)) for _ in range(9)])
    client_num = "+7" + ''.join(client_number)
    enter_phone.send_keys(client_num)
    print(f"Новое имя '{new_name}, новый номер '{client_num}'")

    # сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='UIbutton'])[2]"))).click()
    sleep(0.2)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
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
        sleep(0.1)
        return search_client(browser, client_num)
    except Exception:
        print("Не найден на всех страницах")
        return False

def test_edit_client(browser):
    edit_client(browser)