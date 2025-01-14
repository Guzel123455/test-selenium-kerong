# Права доступа. Добавить пользователя, отредактировать.

from selenium.webdriver import Keys
from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import cprint
from time import sleep
import random

from test_access.access_locators import Locator


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.2)

def edit_user(browser):
    wait = WebDriverWait(browser, 10)

    # user_1
    lastname = f"User_{random.randint(100, 999)}"
    name = f"User_{random.randint(100, 999)}"
    login = f"Admin_{random.randint(100, 999)}"
    password = random.randint(1000, 9999)

    lastname_1 = f"User_new_{random.randint(100, 999)}"
    name_1 = f"User_new_{random.randint(100, 999)}"
    login_1 = f"Admin_new_{random.randint(100, 999)}"
    password_1 = random.randint(1000, 9999)

    cprint("Права доступа. Добавить пользователя, отредактировать / test_func_edit_user", "yellow")

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

    wait.until(EC.element_to_be_clickable((Locator.PASSWORD))).send_keys(password)

    wait.until(EC.element_to_be_clickable((Locator.DOUBLE_PASS))).send_keys(password)

    # Вкладка Права доступа
    wait.until(EC.element_to_be_clickable((Locator.ACCESS))).click()

    # Админ - нет
    wait.until(EC.element_to_be_clickable((Locator.ADMIN))).click()
    wait.until(EC.element_to_be_clickable((Locator.NO_ADMIN))).click()

    # Клиенты. Чтение
    wait.until(EC.element_to_be_clickable((Locator.CLIENT))).click()
    wait.until(EC.element_to_be_clickable((Locator.READ))).click()

    # Сохранить
    wait.until(EC.element_to_be_clickable((Locator.SAVE_BUTTON))).click()
    sleep(1)

    print(f"Создан пользователь: фамилия: '{lastname}', имя: '{name}', логин: '{login}', пароль: {password}")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")


    def edit_user_1(browser):
        # поиск карточки
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
            h2_text = h2_element.text

            # Прокрутка к элементу
            scroll_to_element(browser, h2_element)
            if h2_text == login:

                # открыть карточку
                browser.find_element(By.XPATH, f"//h2[text()= '{login}']").click()
                sleep(1)

                # редактировать
                wait.until(EC.element_to_be_clickable((Locator.EDIT_BUTTON))).click()

                a = wait.until(EC.element_to_be_clickable((Locator.NEW_SURNAME)))
                a.send_keys(Keys.BACKSPACE * 30)
                a.send_keys(lastname_1)

                b = wait.until(EC.element_to_be_clickable((Locator.NEW_NAME)))
                b.send_keys(Keys.BACKSPACE * 30)
                b.send_keys(name_1)

                c = wait.until(EC.element_to_be_clickable((Locator.NEW_LOGIN)))
                c.send_keys(Keys.BACKSPACE * 30)
                c.send_keys(login_1)

                d = wait.until(EC.element_to_be_clickable((Locator.NEW_PASS)))
                d.send_keys(Keys.BACKSPACE * 30)
                d.send_keys(password_1)

                e = wait.until(EC.element_to_be_clickable((Locator.NEW_DOUBLE_PASS)))
                e.send_keys(Keys.BACKSPACE * 30)
                e.send_keys(password_1)

                # Сохранить
                wait.until(EC.element_to_be_clickable((Locator.SAVE_BUTTON))).click()
                sleep(1)

                print(f"Изменен пользователь: фамилия: '{lastname_1}', имя: '{name_1}', логин: '{login_1}', пароль: {password_1}")

                # Получаю текст уведомление
                browser.implicitly_wait(10)
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}")
                return True

        # если карточка не найдена, след старница
        try:
            next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
            next_page.click()
            sleep(0.1)
            return edit_user_1(browser)
        except:
            print("Не найден на всех страницах")
            return False

    # проверка наличия созданной карточки
    if edit_user_1(browser):
        print(f"'{login_1}' - найден")
    else:
        print(f"'{login_1}' - не найден")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")


def test_edit_user(browser):
    edit_user(browser)


