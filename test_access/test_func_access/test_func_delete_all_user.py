# Права доступа. Удалить всех пользователей

from selenium.common import TimeoutException
from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import cprint
from time import sleep
from test_access.access_locators import Locator



def delete_all_user(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Права доступа. Удалить всех пользователей, кроме admin / test_func_delete_all_user", "yellow")

    # Клик по кнопке Настройки
    wait.until(EC.element_to_be_clickable((Locator.SETTINGS_BUTTON))).click()
    wait.until(EC.element_to_be_clickable((Locator.ACCESS_BUTTON))).click()


    user = 0
    while True:
        found = False

        # Обновление списка пользователей
        rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))

        for i in range(len(rows)):
            # Обновим список на каждой итерации
            rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
            h2_element = rows[i].find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
            h2_text = h2_element.text.strip()

            if h2_text != "admin":
                found = True
                # открыть карточку
                h2_element.click()

                # редактировать
                wait.until(EC.element_to_be_clickable((Locator.EDIT_BUTTON))).click()

                # Удалить
                wait.until(EC.element_to_be_clickable((Locator.DELETE))).click()
                wait.until(EC.element_to_be_clickable((Locator.DELETE_USER))).click()
                sleep(0.2)
                user+=1

                # Завершаем цикл после удаления, чтобы перезапустить проверку существующих пользователей
                break

                # Проверка на отсутствие пользователей
        if not found:
            try:
                next_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label = 'Go to next page']")))
                next_page.click()
                sleep(0.2)
            except Exception:
                print(f"Пользователи удалены, кол-во: {user}")
                break

    # Проверка запросов
    for request in browser.requests:
        if request.response and request.response.status_code not in {200, 101, 202}:
            error_message = request.response.body.decode('utf-8')
            print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    # Возврат на первую страницу
    while True:
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Go to previous page']")))
            element.click()
        except TimeoutException:
            break


def test_delete_all_user(browser):
    delete_all_user(browser)
