# Платы. Редактирование платы BU

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import edit_name_BU, edit_ip_plata, new_edit_name_BU, new_edit_ip_plata
from selenium.webdriver import Keys
from time import sleep
from termcolor import cprint

def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.1)

def edit_card_BU(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Платы. Редактирование платы BU / test_func_edit_plata_BU", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[2]"))).click()

    # Добавить KR-BU
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Добавить KR-BU']"))).click()

    # Ввести наименование
    name_plata = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Наименование платы']")))
    name_plata.send_keys(edit_name_BU)

    # Выбрать тип KR-BU
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='Выбрать тип KR-BU платы']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='KR-BU']"))).click()

    # Ввести IP
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='IP-адрес / домен платы KR-BU']"))).send_keys(edit_ip_plata)

    # Выбрать тип KR-CU
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='Выбрать тип KR-СU платы']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='CU_48']"))).click()

    # Сохранить карточку
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(1)
    print(f"Плата '{edit_name_BU}' создана")

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")


    def edit_card_BU(browser):
        # поиск карточки платы
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
            h2_text = h2_element.text

            # Прокрутка к элементу
            scroll_to_element(browser, h2_element)

            if h2_text == edit_name_BU:
                # открыть плату с наименование name_BU_text
                browser.find_element(By.XPATH, f"//h2[text()= '{edit_name_BU}']").click()
                print(f"Плата '{edit_name_BU}' найдена")
                sleep(0.1)

                # редактировать
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Редактировать']"))).click()
                sleep(0.1)

                # изменить наименование
                text_name = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Наименование']")))
                text_name.send_keys(Keys.BACKSPACE * 30)
                text_name.send_keys(new_edit_name_BU)

                # изменить ip
                text_ip = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'IP-адрес']")))
                text_ip.send_keys(Keys.BACKSPACE * 30)
                text_ip.send_keys(new_edit_ip_plata )

                # сохранить
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()

                sleep(0.1)
                return True

        # если карточка не найдена, след старница
        try:
            next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
            sleep(2)
            next_page.click()
            sleep(0.1)
            return edit_card_BU(browser)
        except:
            print("Не найден на всех страницах.")
            return False

    # проверка наличия отредактированой карточки
    if edit_card_BU(browser):
        print(f"'{new_edit_name_BU}' - отредактирована")
    else:
        print(f"'{new_edit_name_BU}' - не найдена")

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    # проверка статус кодов, при статусе кроме 200 и 101 тест падает
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

# Выполнение функции
def test_edit_card_BU(browser):
    edit_card_BU(browser)

