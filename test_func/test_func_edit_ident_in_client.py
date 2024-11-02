# Добавить идентификатор в карточке Клиента

import time
from faker import Faker
from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.1)

def edit_ident_in_client(browser):
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 10)

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # Поиск клиента у которого не привязан идентификатор
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    for row in rows:
        ident = row.find_element(By.CSS_SELECTOR, "td:nth-child(3) h2")
        ident_text = ident.text

        # открытие клиента и выбор идентифкатора
        if ident_text == '':
            # имя клиента
            name = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h4")
            print(f"Выбран клиент '{name.text}'")
            actions.move_to_element(row).click().perform()
            time.sleep(0.1)

            # Кнопка "Добавить"
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить']"))).click()
            time.sleep(0.1)

            # Выбрать ТИ
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'demo-simple-select-helper']"))).click()
            time.sleep(0.1)
            # Клик по идентификатору
            type = browser.find_element(By.CSS_SELECTOR, "li:nth-child(1)")
            print(f"Клиенту привязан идентификатор '{type.text}'")
            type.click()
            time.sleep(0.1)

            # ввести значение идентификатора
            ident = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[6]")))
            ident.click()
            fake = Faker("ru_RU")
            ident_1 = fake.postcode()
            ident.send_keys(ident_1)
            print(f"Со значением '{ident_1}'")

            # сохранить
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Сохранить']"))).click()
            time.sleep(0.1)

            # Получаю текст уведомление
            text_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id= 'notistack-snackbar']")))
            text_message_txt = text_message.text
            print(f"Текст уведомления: {text_message_txt}")
            time.sleep(0.1)
            break

        for request in browser.requests:
            if request.response:
                if request.response.status_code not in {200, 101}:
                    error_message = request.response.body.decode('utf-8')
                    print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    # Если не найден, клик на следующую страницу
    try:
        next_page = browser.find_element(By.XPATH, "//button[@aria-label='Go to next page']")
        next_page.click()
        # рекурсивный вызов функции
        return edit_ident_in_client(browser)
    except:
        return False

def test_edit_ident_in_client(browser):
    edit_ident_in_client(browser)