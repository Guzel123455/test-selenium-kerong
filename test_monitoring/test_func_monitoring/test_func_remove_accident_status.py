# Мониторинг. Зона. Снять статус авария

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
from config import name_zone_publ
from time import sleep


def remove_accident_status(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Мониторинг. Зона. Снять статус авария / test_func_remove_accident_status", "yellow")

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()
    sleep(1)

    # Все ячейки
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"В зоне '{name_zone_publ}' кол-во ячеек: {len(cells)}")

    acc_cell = False
    for cell in cells:
        # Ячейки "Авария"
         accident = cell.find_elements(By.XPATH, "//div[text() = 'Авария']")

         if accident:
            try:
                # Клик на свободную ячейку
                browser.execute_script("arguments[0].click();", accident[0])

                # Получить номер ячейки
                num = browser.find_element(By.XPATH, "//div/h2")
                num_text = num.get_attribute("innerText")

                # Клик на Авария
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class = 'back-to'])[2]"))).click()

                # снять аварию
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class = 'back-to'])[4]"))).click()
                print(f"С '{num_text}' снят статус Авария")
                sleep(1)

                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}")

                for request in browser.requests:
                    if request.response:
                        if request.response.status_code not in {200, 101, 201}:
                            error_message = request.response.body.decode('utf-8')
                            print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

                acc_cell = True
                break
            except Exception as e:
                print(f"Ошибка: {str(e)}")

    if not acc_cell:
        print(f"Нет ячеек со статусом Авария")

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

            break

def test_remove_accident_status(browser):
    remove_accident_status(browser)


