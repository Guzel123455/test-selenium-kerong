# Мониторинг. Зона. Выбрать свободную ячейку. Установить статус 'Авария'

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import name_zone_publ
from time import sleep
from termcolor import cprint


def status_of_accident_in_free_cell(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Мониторинг. Зона. Выбрать свободную ячейку. Установить статус 'Авария' / test_func_status_of_accident_in_free_cell", "yellow")

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()
    sleep(1)

    # Все ячейки
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"В зоне '{name_zone_publ}' кол-во ячеек: {len(cells)}")

    free_cell = False
    for cell in cells:
        # Свободные ячейки
        free = cell.find_elements(By.XPATH, "//div[@class ='free']")

        if free:
            try:
                # Клик на свободную ячейку
                browser.execute_script("arguments[0].click();", free[0])

                # Получить номер ячейки
                num = browser.find_element(By.XPATH, "//div/h2")
                num_text = num.get_attribute("innerText")

                # Клик на Авария
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class = 'back-to'])[2]"))).click()

                # Установить Аварию
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class = 'back-to'])[3]"))).click()
                print(f"Создана авария на '{num_text}'")
                sleep(1)

                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-2].text
                    print(f"Текст уведомления: {last_notification_text}")

                for request in browser.requests:
                    if request.response:
                        if request.response.status_code not in {200, 101, 201}:
                            error_message = request.response.body.decode('utf-8')
                            print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

                free_cell = True
                break
            except Exception as e:
                print(f"Ошибка: {str(e)}")

    if not free_cell:
        print(f"Нет свободных ячеек")

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

def test_status_of_accident_in_free_cell(browser):
    status_of_accident_in_free_cell(browser)