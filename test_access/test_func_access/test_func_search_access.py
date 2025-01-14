# Права доступа. Поле поиск

from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import TimeoutException
from termcolor import cprint
from time import sleep
import random
from test_access.access_locators import Locator



def search_access(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    cprint("Права доступа. Поле Поиск / test_func_search_access1", "yellow")

    # клик по кнопке Настройки
    wait.until(EC.element_to_be_clickable((Locator.SETTINGS_BUTTON))).click()

    # Права доступа
    wait.until(EC.element_to_be_clickable((Locator.ACCESS_BUTTON))).click()
    sleep(0.2)

    # данные всех пользователей на первой странице
    list_login = []
    list_name = []
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    for row in rows:
        login = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
        login_text = login.text
        if login_text:
            list_login.append(login_text)

        name = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
        name_text = name.text.split()[0] if name.text else ''
        if name_text:
            list_name.append(name_text)
        # name_text_2 = name.text.split()[1] if name.text else ''
        # if name_text_2:
        #     list_name.append(name_text_2)
    print(f"Все логины со страницы 1: {list_login}")
    print(f"Все имена со страницы 1: {list_name}")
    print()


    # Поиск — выбор случайного значения и отправка в строку поиска
    if list_login:  # Проверяем, что список не пуст
        random_login = random.choice(list_login)  # Выбираем случайное значение
        print("Значение для поиска:", random_login)

        # поиск
        search = wait.until(EC.element_to_be_clickable((Locator.SEARCH)))
        search.send_keys(random_login)
        sleep(1)

        try:
            WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
            rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
            found_count = 0
            for row in rows:
                try:
                    h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
                    h2_text = h2_element.text.strip()

                    if h2_text == random_login:
                        found_count += 1
                        actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                        sleep(0.1)
                except Exception:
                    continue
            print(f"Количество найденных строк по логину: {found_count}")
            print()
            if found_count == 0:
                print(f"{random_login} - значение не найдено")
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(0.1)
        except TimeoutException:
            print("Нет значений")

    if list_name:
        random_name = random.choice(list_name)
        print("Значение для поиска:", random_name)

        # поиск
        search = wait.until(EC.element_to_be_clickable((Locator.SEARCH)))
        search.send_keys(random_name)
        sleep(1)

        try:
            WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
            rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
            found_count = 0
            for row in rows:
                try:
                    h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
                    h2_text = h2_element.text.strip()
                    first_name = h2_text.split()[0]
                    if first_name == random_name:
                        found_count += 1
                        actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                except Exception:
                    continue
            print(f"Количество найденных строк по имени: {found_count}")
            print()
            if found_count == 0:
                print(f"{random_name} - значение не найдено")
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(0.1)
        except TimeoutException:
            print("Нет значений")



def test_search_access(browser):
    search_access(browser)