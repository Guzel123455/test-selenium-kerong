# Мoниторинг. Зона. Открыть - По статусу - Занятые ячейки

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from termcolor import cprint
from config import name_zone_publ
from selenium.webdriver.common.keys import Keys
from time import sleep

def click_empty_space(browser):
    actions = ActionChains(browser)
    actions.move_by_offset(0, 0).click().perform()


def open_lock_rent(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    cprint("Мoниторинг. Зона. Открыть - По статусу - Занятые ячейки / test_func_open_rent_lock_in_zona", "yellow")

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()
    sleep(0.1)

    # Открыть зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()
    sleep(0.1)

    # количество ячеек
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"В зоне '{name_zone_publ}' кол-во ячеек: {len(cells)}")

    lock_all = browser.find_elements(By.CLASS_NAME, "lock-item-container")
    locks_num = 0

    for l in lock_all:
        try:

            # статус ячейки -занят
            lock_name_busy = l.find_element(By.XPATH, ".//div[@class='rent']").text

            if lock_name_busy:
                locks_num += 1

                # Нажимаем Открыть
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Открыть']"))).click()

                # Открываем ячейку по статусу Занятые
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'по статусу']"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать статус ячейки']"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Занятые']"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()= 'Открыть'])[2]"))).click()
                sleep(3)


        except:
            pass

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    print(f"Количество занятых ячеек: {locks_num}")
    actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101, 201}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")



def test_open_lock_rent(browser):
    open_lock_rent(browser)
