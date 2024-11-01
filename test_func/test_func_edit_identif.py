# добавление идентиф , редактирование

import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import edit_identif, new_edit_identif, new_edit_type_identif
from browser_setup import browser

def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.1)

def edit_ident(browser):
    wait = WebDriverWait(browser, 20)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[5]"))).click()

    # Клик по кнопке Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Добавить']"))).click()

    # Выбрать тип идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'demo-simple-select-helper']"))).click()

    # Прокручиваем до нужного элемента типа идентификатора
    option_to_select = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text()= '{new_edit_type_identif}']")))
    browser.execute_script("arguments[0].scrollIntoView();", option_to_select)
    time.sleep(0.5)
    option_to_select.click()

    # Ввести значение
    name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name.send_keys(edit_identif)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    time.sleep(0.1)
    print(f"Карточка '{edit_identif}' создана")

    def edit_iden(browser):
        # поиск карточки
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
            h2_text = h2_element.text

            # Прокрутка к элементу
            scroll_to_element(browser, h2_element)

            if h2_text == edit_identif:
                # открыть карточку
                browser.find_element(By.XPATH, f"//h2[text()= '{edit_identif}']").click()
                #time.sleep(0.1)

                # редактировать
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Редактировать']"))).click()
                #time.sleep(0.1)

                # изменить тип идентификатора
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'MuiInputAdornment-root MuiInputAdornment-positionEnd MuiInputAdornment-outlined MuiInputAdornment-sizeMedium css-1nvf7g0']"))).click()

                # Ввести наименование
                name_zone = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
                name_zone.send_keys(Keys.BACKSPACE * 30)
                name_zone.send_keys(new_edit_identif)
                #time.sleep(0.1)

                # Сохранить
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
                time.sleep(0.1)
                return True

        # если карточка не найдена, след старница
        try:
            next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
            next_page.click()
            time.sleep(0.1)
            return edit_iden(browser)
        except:
            print("Не найден на всех страницах")
            return False

    # проверка наличия созданной карточки
    if edit_iden(browser):
        print(f"'{new_edit_identif}' - отредактирована")
    else:
        print(f"'{new_edit_identif}' - не найден")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
        #       pytest.fail()

# Выполнение функции
def test_edit_ident(browser):
    edit_ident(browser)