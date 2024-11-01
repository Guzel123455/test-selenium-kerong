# добавление публичной зоны и редактирование

import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import edit_name_zone_publ, edit_num_from_publ, edit_num_to_publ, new_edit_name_zone_publ, new_edit_num_from_publ, new_edit_num_to_publ
from browser_setup import browser

def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.1)

def edit_zone_publ(browser):
    wait = WebDriverWait(browser, 20)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик на Зоны
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[1]"))).click()

    # Клик на Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'UIbutton']"))).click()

    # Ввести наименование
    name_zone = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name_zone.send_keys(edit_name_zone_publ)

    # Номера От
    num1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[3]")))
    num1.send_keys(Keys.CONTROL, "a")
    num1.send_keys(edit_num_from_publ)

    # Номера До
    num2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[4]")))
    num2.send_keys(Keys.CONTROL, "a")
    num2.send_keys(edit_num_to_publ)

    # Режим доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'demo-simple-select-helper']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Публичный']"))).click()

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    time.sleep(0.2)
    print(f"Зона '{edit_num_from_publ}' создана")

    def edit_zona(browser):
        # поиск карточки платы
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
            h2_text = h2_element.text

            # Прокрутка к элементу
            scroll_to_element(browser, h2_element)

            if h2_text == edit_name_zone_publ:
                # открыть зону
                browser.find_element(By.XPATH, f"//h2[text()= '{edit_name_zone_publ}']").click()
                time.sleep(0.1)

                # редактировать
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Редактировать']"))).click()
                time.sleep(0.1)

                # Ввести наименование
                name_zone = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
                name_zone.send_keys(Keys.BACKSPACE * 30)
                name_zone.send_keys(new_edit_name_zone_publ)
                time.sleep(0.1)

                # Номера От
                num1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[3]")))
                num1.send_keys(Keys.CONTROL, "a")
                num1.send_keys(new_edit_num_from_publ)

                # Номера До
                num2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[4]")))
                num2.send_keys(Keys.CONTROL, "a")
                num2.send_keys(new_edit_num_to_publ)

                # сохранить
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
                time.sleep(0.2)
                return True

        # если карточка не найдена, след старница
        try:
            next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
            next_page.click()
            time.sleep(0.1)
            return edit_zona(browser)
        except:
            print("Не найден на всех страницах")
            return False

    # проверка наличия созданной карточки
    if edit_zona(browser):
        print(f"{new_edit_name_zone_publ} - найден")
        print()
    else:
        print(f"{new_edit_name_zone_publ} - не найден")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print( f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
#                pytest.fail()

# Выполнение функции
def test_edit_zone_publ(browser):
    edit_zone_publ(browser)




