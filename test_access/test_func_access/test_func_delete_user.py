# Права доступа. Удалить пользователя

from selenium.common import TimeoutException
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

def delete_user(browser):
    wait = WebDriverWait(browser, 10)

    # user_7
    lastname7 = f"Фамилия{random.randint(100, 999)}"
    name7 = f"Имя{random.randint(100, 999)}"
    login7 = f"Admin_{random.randint(100, 999)}"
    password7 = random.randint(100, 999)

    cprint("Права доступа. Добавить пользователя. User_4 / test_func_add_user_4", "yellow")

    # клик по кнопке Настройки
    wait.until(EC.element_to_be_clickable((Locator.SETTINGS_BUTTON))).click()

    # Права доступа
    wait.until(EC.element_to_be_clickable((Locator.ACCESS_BUTTON))).click()

    # Добавить пользователя
    wait.until(EC.element_to_be_clickable((Locator.ADD_USER))).click()

    # Заполнить поля Фамилия, Имя, Логин, Пароль, Подтверждение пароля

    wait.until(EC.element_to_be_clickable((Locator.SURNAME))).send_keys(lastname7)

    wait.until(EC.element_to_be_clickable((Locator.NAME))).send_keys(name7)

    wait.until(EC.element_to_be_clickable((Locator.LOGIN))).send_keys(login7)

    wait.until(EC.element_to_be_clickable((Locator.PASSWORD))).send_keys(password7)

    wait.until(EC.element_to_be_clickable((Locator.DOUBLE_PASS))).send_keys(password7)

    # Вкладка Права доступа
    wait.until(EC.element_to_be_clickable((Locator.ACCESS))).click()

    # Админ - нет
    wait.until(EC.element_to_be_clickable((Locator.ADMIN))).click()
    wait.until(EC.element_to_be_clickable((Locator.NO_ADMIN))).click()

    # Аренда. Чтение
    wait.until(EC.element_to_be_clickable((Locator.RENT))).click()
    wait.until(EC.element_to_be_clickable((Locator.READ))).click()

    print(f"Создан пользователь '{login7}' с паролем '{password7}' с правами доступа: Аренда. Чтение.")

    # Сохранить
    wait.until(EC.element_to_be_clickable((Locator.SAVE_BUTTON))).click()
    sleep(0.2)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")


    found = False
    while not found:
        rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))

        for row in rows:
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
            h2_text = h2_element.text

            # Прокрутка к элементу
            scroll_to_element(browser, h2_element)

            if h2_text == login7:
                found = True
                # открыть карточку
                h2_element.click()

                # редактировать
                wait.until(EC.element_to_be_clickable((Locator.EDIT_BUTTON))).click()

                # Удалить
                wait.until(EC.element_to_be_clickable((Locator.DELETE))).click()
                wait.until(EC.element_to_be_clickable((Locator.DELETE_USER))).click()
                sleep(0.2)

                # Проверка, что карточка удалена
                rows_after_delete = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
                if not any(login7 in row.text for row in rows_after_delete):
                    print(f"'{login7}' - удалена")
                else:
                    print(f"'{login7}' - не удалена")
                break

        # Перейти на следующую страницу, если карточка не была найдена
        if not found:
            try:
                next_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label = 'Go to next page']")))
                next_page.click()
                sleep(0.2)
            except Exception:
                print("Не найден на всех страницах")
                return False

        # Блок для проверки запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101, 202}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")


    # возврат на первую страницу
    while True:
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label = 'Go to previous page']")))
            element.click()
        except TimeoutException:
            break

    # показать неактивных пользователей
    wait.until(EC.element_to_be_clickable((Locator.INACTIVE_USER))).click()

      # проверка наличия созданной карточки
    if search(browser, login7):
        print()
    else:
        print(f"{login7} - не найден.")

def search(browser, login7):
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

    # Проверяем каждую строку на наличие текста
    for row in rows:
        h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
        h2_text = h2_element.text.strip()

        # Прокрутка к элементу
        scroll_to_element(browser, h2_element)

        if h2_text == login7:
            print(f"{h2_text} - найден в списке 'Неактивных пользователей'")
            return True

    # Если карточка не найдена, клик на следующую страницу
    try:
        next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
        next_page.click()
        # рекурсивный вызов функции
        return search(browser, login7)
    except:
        print("Не найден на всех страницах")
        return False



def test_delete_user(browser):
    delete_user(browser)

