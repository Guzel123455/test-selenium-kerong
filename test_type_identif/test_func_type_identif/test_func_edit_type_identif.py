# Добавление ТИ, редактирование

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import random
from time import sleep
from termcolor import cprint


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.1)

def edit_type_ident(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Добавление ТИ, редактирование / test_func_edit_type_identif", "yellow")

    # Редактирование типа идентификатора
    edit_type_identif = f"ТИ_тест_{random.randint(10, 99)}"
    new_edit_type_identif = f"ТИ_тест_изменен_{random.randint(10, 99)}"

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Типы идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[4]"))).click()

    # Клик по кнопке Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Добавить']"))).click()

    # Ввести наименование
    name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Наименование']")))
    name.send_keys(edit_type_identif)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    sleep(0.2)
    print(f"Создан тип идентификатора '{edit_type_identif}'")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    def edit_type_ident(browser):
        # поиск карточки
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
            h2_text = h2_element.text

            # Прокрутка к элементу
            scroll_to_element(browser, h2_element)

            if h2_text == edit_type_identif:
                # открыть карточку
                browser.find_element(By.XPATH, f"//h2[text()= '{edit_type_identif}']").click()

                # редактировать
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Редактировать']"))).click()

                # Ввести наименование
                name_zone = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Наименование']")))
                name_zone.send_keys(Keys.BACKSPACE * 30)
                name_zone.send_keys(new_edit_type_identif)

                # Сохранить
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()

                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}")

                sleep(0.1)
                return True

        # если карточка не найдена, след старница
        try:
            next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
            next_page.click()
            sleep(0.1)
            return edit_type_ident(browser)
        except:
            print("Не найден на всех страницах")
            return False

    # проверка наличия созданной карточки
    if edit_type_ident(browser):
        print(f"'{new_edit_type_identif}' - отредактирован")
    else:
        print(f"'{new_edit_type_identif}' - не найден")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
        #       pytest.fail()

# Выполнение функции
def test_edit_type_ident(browser):
    edit_type_ident(browser)