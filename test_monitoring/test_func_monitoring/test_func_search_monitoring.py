# Мониторинг. Зона. Строка поиска

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser_setup import browser
from selenium.webdriver.common.action_chains import ActionChains
from termcolor import cprint
from time import sleep
from selenium.webdriver.common.keys import Keys


def search_monitoring(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    cprint("Мониторинг. Зона. Строка поиска / test_func_search_monitoring", "yellow")

    # Нажимаем на кнопку "Мониторинг"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    found_zone_with_locks = False
    # все зоны
    zones = browser.find_elements(By.XPATH, "//div/h2[@style]")
    zone_count = len(zones)
    print(f'Всего зон: {zone_count}')

    for i in range(zone_count):
        zone = zones[i]
        zone_name = zone.text
        zone.click()
        sleep(1)

        # Проверяем количество ячеек
        cells = browser.find_elements(By.CLASS_NAME, 'lock-item-container')
        cell_count = len(cells)


        if cell_count > 0:
            found_zone_with_locks = True

            cells = browser.find_elements(By.CLASS_NAME, 'lock-item-container')
            first_num = cells[0].find_element(By.CLASS_NAME, 'title').text
            last_num = cells[-1].find_element(By.CLASS_NAME, 'title').text
            print(f"В '{zone_name}' нумерация ячеек с '{first_num[7:]}' по '{last_num[7:]}'")

            # строка поиска
            search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Поиск по номеру замка']")))
            search.send_keys(last_num[7:])
            print(f"Поиск по номеру ячейки '{last_num[7:]}'")
            sleep(1)

            cells = browser.find_elements(By.CLASS_NAME, 'lock-item-container')
            a = cells[-1].find_element(By.CLASS_NAME, 'title').text[7:]
            if a == last_num[7:]:
                print(f"'Ячейка {a}' найдена")
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(0.2)
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
            if request.response.status_code not in {200, 101, 201}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")


def test_search_monitoring(browser):
    search_monitoring(browser)
