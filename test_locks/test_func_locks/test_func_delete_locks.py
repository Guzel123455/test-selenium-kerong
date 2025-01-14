# Замки и ячейки. Удаление набора замков, первый в списке

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

def delete_locks(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Замки и ячейки. Удаление набора замков, первый в списке / test_func_delete_locks", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик на замки и ячейки
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'settings-item'])[3]"))).click()

    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

    if rows:
        # Получаем наименование первого набора замков
        first_lock_set_name = rows[0].find_element(By.CSS_SELECTOR, "td:nth-child(1) h2").text
        print(f"Удаляемый набор замков: '{first_lock_set_name}'")

        # Удаление первого набора замков
        wait.until(EC.element_to_be_clickable((rows[0].find_element(By.CSS_SELECTOR, "svg")))).click()
        sleep(1)

        # Получаю текст уведомления
        notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
        if notifications:
            last_notification_text = notifications[-1].text
            print(f"Текст уведомления: {last_notification_text}")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")


def test_delete_locks(browser):
    delete_locks(browser)