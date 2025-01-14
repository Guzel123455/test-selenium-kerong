# Мониторинг. Открыть зону, получить список замков

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser_setup import browser
from termcolor import cprint

def open_monitor(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Мониторинг. Открыть зону, получить список замков / test_func_open_zone_monitoring", "yellow")

    # Нажимаем на кнопку "Мониторинг"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    found_zone_with_locks = False

    # все зоны
    zones = browser.find_elements(By.XPATH, "//div/h2[@style]")
    zone_count = len(zones)
    print(f"Всего зон: '{zone_count}'")

    for i in range(zone_count):
        zone = zones[i]
        zone_name = zone.text
        zone.click()
        sleep(0.2)

        # Проверяем количество ячеек
        cells = browser.find_elements(By.CLASS_NAME, 'lock-item-container')
        cell_count = len(cells)
        print(f"'{zone_name}' кол-во ячеек {cell_count}")

        if cell_count > 0:
            found_zone_with_locks = True
            first_num = cells[0].find_element(By.CLASS_NAME, 'title').text
            last_num = cells[-1].find_element(By.CLASS_NAME, 'title').text
            print(f"C '{first_num}' по '{last_num}'")
            break
        else:
            print(f'В зоне "{zone_name}" замков нет')

            browser.find_element(By.CLASS_NAME, 'back-to').click()
            sleep(0.2)

            # Перезагружаем список зон
            zones = browser.find_elements(By.XPATH, "//div/h2[@style]")

    if not found_zone_with_locks:
        print('Нет зон с замками')

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")


def test_open_monitor(browser):
    open_monitor(browser)
