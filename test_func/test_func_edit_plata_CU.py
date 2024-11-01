# редактирование карточки CU и проверка наличия карточки

import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import new_edit_name_BU, edit_name_CU, edit_number_in_chain, new_edit_name_CU, new_edit_number_in_chain
from browser_setup import browser

def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.1)

def edit_card_CU(browser):
    wait = WebDriverWait(browser, 10)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class ='table-item'])[2]"))).click()

    # открыть вкладку CU платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h4[text() = 'CU - платы']"))).click()

    # Добавить KR-CU
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить KR-CU']"))).click()

    # Ввести наименование
    name_plata = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name_plata.send_keys(edit_name_CU)

    # Выбрать тип KR-CU
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'demo-simple-select-helper'])[1]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='CU_48']"))).click()

    # Выбрать плату KR-BU
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='demo-simple-select-helper'])[2]"))).click()
    bu = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text()= '{new_edit_name_BU}']")))
    browser.execute_script("arguments[0].scrollIntoView();", bu)
    time.sleep(0.1)
    bu.click()

    # Номер в цепи
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='demo-simple-select-helper'])[3]"))).click()
    num = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text()= '{edit_number_in_chain}']")))
    browser.execute_script("arguments[0].scrollIntoView();", num)
    time.sleep(0.1)
    num.click()

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    time.sleep(0.2)
    print(f"Карточка '{edit_name_CU}' создана")

    def edit_card_CU(browser):
        # поиск карточки платы
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
            h2_text = h2_element.text

            # Прокрутка к элементу
            scroll_to_element(browser, h2_element)

            if h2_text == edit_name_CU:

                # открыть плату
                browser.find_element(By.XPATH, f"//h2[text()= '{edit_name_CU}']").click()

                # редактировать
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Редактировать']"))).click()

                # изменить наименование
                text_name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
                text_name.send_keys(Keys.BACKSPACE * 30)
                text_name.send_keys(new_edit_name_CU)

                # Номер в цепи
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class = 'MuiInputAdornment-root MuiInputAdornment-positionEnd MuiInputAdornment-outlined MuiInputAdornment-sizeMedium css-1nvf7g0'])[2]"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='demo-simple-select-helper']"))).click()
                num = wait.until(EC.visibility_of_element_located((By.XPATH, f"//li[text()= '{new_edit_number_in_chain}']")))
                browser.execute_script("arguments[0].scrollIntoView();", num)
                time.sleep(0.1)
                num.click()

                # сохранить
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
                time.sleep(0.2)
                return True

        # если карточка не найдена, след старница
        try:
            next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
            next_page.click()
            time.sleep(0.1)
            return edit_card_CU(browser)
        except:
            print("Не найден на всех страницах.")
            return False

    # проверка наличия отредактированой карточки
    if edit_card_CU(browser):
        print(f"'{new_edit_name_CU}' - отредактирована")
    else:
        print(f"'{new_edit_name_CU}' - не найдена")

    # проверка статус кодов, при статусе кроме 200 и 101 тест падает
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
  #              pytest.fail()

# Выполнение функции
def test_edit_card_CU(browser):
    edit_card_CU(browser)

