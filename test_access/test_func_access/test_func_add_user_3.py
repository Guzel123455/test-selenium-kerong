# Права доступа. Добавить пользователя и авторизоваться. User_3

from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import cprint
from time import sleep
import random
from config import log_in, password
from test_access.access_locators import Locator


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.2)

def user_3(browser):
    wait = WebDriverWait(browser, 10)

    # user_3
    lastname = f"lastname_{random.randint(100, 999)}"
    name = f"name_{random.randint(100, 999)}"
    login = f"Admin_3_{random.randint(100, 999)}"
    passwordd = random.randint(1000, 9999)

    cprint("Права доступа. Добавить пользователя с правами доступа: Отчеты. User_3 / test_func_add_user_3", "yellow")

    # клик по кнопке Настройки
    wait.until(EC.element_to_be_clickable((Locator.SETTINGS_BUTTON))).click()

    # Права доступа
    wait.until(EC.element_to_be_clickable((Locator.ACCESS_BUTTON))).click()

    # Добавить пользователя
    wait.until(EC.element_to_be_clickable((Locator.ADD_USER))).click()

    # Заполнить поля Фамилия, Имя, Логин, Пароль, Подтверждение пароля

    wait.until(EC.element_to_be_clickable((Locator.SURNAME))).send_keys(lastname)

    wait.until(EC.element_to_be_clickable((Locator.NAME))).send_keys(name)

    wait.until(EC.element_to_be_clickable((Locator.LOGIN))).send_keys(login)

    wait.until(EC.element_to_be_clickable((Locator.PASSWORD))).send_keys(passwordd)

    wait.until(EC.element_to_be_clickable((Locator.DOUBLE_PASS))).send_keys(passwordd)

    # Вкладка Права доступа
    wait.until(EC.element_to_be_clickable((Locator.ACCESS))).click()

    # Админ - нет
    wait.until(EC.element_to_be_clickable((Locator.ADMIN))).click()
    wait.until(EC.element_to_be_clickable((Locator.NO_ADMIN))).click()

    # Отчеты
    wait.until(EC.element_to_be_clickable((Locator.REPORTS))).click()
    wait.until(EC.element_to_be_clickable((Locator.REPORTS_YES))).click()

    # Сохранить
    wait.until(EC.element_to_be_clickable((Locator.SAVE_BUTTON))).click()
    sleep(1)

    print(f"Создан пользователь '{login}' с паролем '{passwordd}'. Права доступа: 'Отчеты'")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    # проверка наличия созданной карточки
    if search(browser, login):
        print(f"{login} - найден в списке пользователей")
    else:
        print(f"{login} - не найден в списке пользователей")

    # выйти из учетки admin
    wait.until(EC.element_to_be_clickable((Locator.LOG_OUT))).click()

    wait.until(EC.element_to_be_clickable((Locator.LOG_OUT_2))).click()

    # ввести логин
    wait.until(EC.element_to_be_clickable((Locator.INPUT_LOGIN))).send_keys(login)

    # ввести пароль
    wait.until(EC.element_to_be_clickable((Locator.INPUT_PASS))).send_keys(passwordd)

    # клик по кнопке войти
    wait.until(EC.element_to_be_clickable((Locator.LOG_IN))).click()
    sleep(1)

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    sections(browser)

def sections(browser):
    wait = WebDriverWait(browser, 10)

    # Ждем загрузку бокового меню
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "side-menu-items-container")))

    # Получаем все кнопки-разделы на боковой панели
    sections = browser.find_elements(By.CSS_SELECTOR, ".menu-items, .menu-items-focus")

    # должны отображаться Мониторинг, отчеты
    visible_sections = [section.text for section in sections]
    print("У пользователя 'user_3' отображаются разделы:")
    for section in sections:
        print(f"- {section.text}")

        # Проверка на наличие разделов, которые не должны отображаться
    not_visible = ["Клиенты", "Справочники", "Настройки"]
    for section in not_visible:
        assert section not in visible_sections, f"Ошибка: Раздел '{section}' отображается"

        print(f"Раздел '{section}' не отображается")

    # выйти из учетки admin
    wait.until(EC.element_to_be_clickable((Locator.LOG_OUT))).click()
    wait.until(EC.element_to_be_clickable((Locator.LOG_OUT_2))).click()

    # ввести логин
    wait.until(EC.element_to_be_clickable((Locator.INPUT_LOGIN))).send_keys(log_in)

    # ввести пароль
    wait.until(EC.element_to_be_clickable((Locator.INPUT_PASS))).send_keys(password)

    # клик по кнопке войти
    wait.until(EC.element_to_be_clickable((Locator.LOG_IN))).click()
    sleep(1)


def search(browser, login):
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

    # Проверяем каждую строку на наличие текста
    for row in rows:
        h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
        h2_text = h2_element.text.strip()

        # Прокрутка к элементу
        scroll_to_element(browser, h2_element)

        if h2_text == login:
            return True

    # Если карточка не найдена, клик на следующую страницу
    try:
        next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
        next_page.click()
        # рекурсивный вызов функции
        return search(browser, login)
    except:
        print("Не найден на всех страницах")
        return False

def test_user_3(browser):
    user_3(browser)




