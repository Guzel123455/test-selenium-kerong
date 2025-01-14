# Клиенты. Открыть карточку клиента. Пароль приложения


from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from termcolor import cprint

def add_password_in_client(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Открыть карточку клиента. Пароль приложения / test_func_add_password_in_client", "yellow")

    # открыть вкладку Пароль приложения
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Пароль приложения']"))).click()
    sleep(1)

    # сгенерировать пароль
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Сгенерировать пароль']"))).click()
    sleep(1)

    # значение пароля
    pas = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div/h2)[1]"))).text
    print(f"Пароль приложения '{pas}'")

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


def test_add_password_in_client(browser):
    add_password_in_client(browser)