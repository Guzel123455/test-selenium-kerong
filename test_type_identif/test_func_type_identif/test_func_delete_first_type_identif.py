#  Тип идентификатора. Удаление первого в списке тип идентификатора

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from termcolor import cprint


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.1)

def delete_first_type_identif(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Тип идентификатора. Удаление первого в списке тип идентификатора / test_func_delete_first_type_identif", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по тип идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[4]"))).click()
    sleep(1)

    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

    if rows:
        # Получаем наименование первого типа идентификатора в списке
        first_type_ident = rows[0].find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
        sleep(1)
        first_type_ident_text = first_type_ident.text
        print(f"Удаляемый идентификатор: '{first_type_ident_text}'")
        first_type_ident.click()

        # редактировать
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Редактировать']"))).click()

        # Удалить
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Удалить']"))).click()
        sleep(1)

        # Получаю текст уведомления
        notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
        if notifications:
            last_notification_text = notifications[-1].text
            print(f"Текст уведомления: {last_notification_text}")

            text_1 = "Чтобы удалить тип идентификатора, который принимал участие в операциях - необходимо использовать флаг force=true"
            text_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id= 'notistack-snackbar']")))
            text_message_txt = text_message.text

            if text_1.strip() == text_message_txt.strip():
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Удалить'])[2]"))).click()
                sleep(1)

    # Блок для проверки запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                # pytest.fail()


def test_delete_first_type_identif(browser):
    delete_first_type_identif(browser)