# Мониторинг. Зона. Снять все аренды (будущие и текущие)

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from config import name_zone_publ
from termcolor import cprint



def delete_all_rent(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    cprint("# Мониторинг. Зона. Снять все аренду(будущие и текущие) / test_func_delete_all_rent", "yellow")

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()

    # Все ячейки
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"В зоне '{name_zone_publ}' кол-во ячеек: {len(cells)}")

    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))

    for cell in cells:

        # занятые ячейки
        rent = cell.find_elements(By.XPATH, "//div[@class ='rent']")

        if rent:

            # Клик на занятую ячейку
            browser.execute_script("arguments[0].click();", rent[0])
            sleep(1)
            s = browser.find_element(By.XPATH, "//div/h2").text
            print(f"Снять аренду с '{s}'")

            try:
                a = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Снять аренду']")))
                a.click()
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(10)


                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}")



            except:
                # Если кнопка не найдена, открыть "Будущие аренды"
                b = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Будущие аренды']")))
                b.click()

                delete_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"svg > path[d='M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6zM19 4h-3.5l-1-1h-5l-1 1H5v2h14z']")))
                delete_button.click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Снять аренду']"))).click()
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(10)


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


def test_delete_all_rent(browser):
    delete_all_rent(browser)
