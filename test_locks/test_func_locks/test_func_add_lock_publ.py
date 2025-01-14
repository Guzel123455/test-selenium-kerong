# Замки и ячейки. Создание набора замков для публичной зоны

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_func.func_search import search_line
from selenium.webdriver import Keys
from time import sleep
from termcolor import cprint
from config import name_BU_text, name_CU_text, name_zone_publ, name_lock_publ, num_to_publ, num_from_publ


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.5)

def add_lock_publ(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Замки и ячейки. Создание набора замков для публичной зоны / test_func_add_lock_publ", "yellow")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик на замки и ячейки
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'settings-item'])[3]"))).click()

    # Клик на Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'UIbutton']"))).click()

    # Выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать зону']"))).click()
    zona = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{name_zone_publ} [{num_from_publ}-{num_to_publ}]')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", zona)
    zona.click()

    # Ввести наименование
    name_lock = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Название набора']")))
    name_lock.send_keys(name_lock_publ)

    # Стартовый номер
    start_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'Стартовый номер'])[1]")))
    start_num.send_keys(Keys.CONTROL, "a")
    start_num.send_keys(num_from_publ)

    # Конечный номер
    stop_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'Конечный номер'])[1]")))
    stop_num.send_keys(Keys.CONTROL, "a")
    stop_num.send_keys(num_to_publ)

    # Колво ячеек
    #count_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[5]")))
    #count_num.send_keys(Keys.CONTROL, "a")
    #count_num.send_keys(count_lock_publ)

    # Выбрать BU плату
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать KR-BU плату']"))).click()
    b = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{name_BU_text}')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", b)
    browser.execute_script("arguments[0].click();", b)

    # Выбрать CU плату
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать KR-CU плату']"))).click()
    c = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{name_CU_text}')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", c)
    browser.execute_script("arguments[0].click();", c)

    # Стартовый номер на плате
    start_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'Стартовый номер'])[2]")))
    start_num.send_keys(Keys.CONTROL, "a")
    start_num.send_keys(str(int(num_from_publ)-1))

    # Конечный номер на плате
    stop_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'Конечный номер'])[2]")))
    stop_num.send_keys(Keys.CONTROL, "a")
    stop_num.send_keys(str(int(num_to_publ)-1))

    # Колво плате
    #count_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[9]")))
    #count_num.send_keys(Keys.CONTROL, "a")
    #count_num.send_keys(count_plata_publ)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(1)
    print(f"Набор замков '{name_lock_publ}' создан")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    if search_line(browser, name_lock_publ):
        print()
    else:
        print(f"{name_lock_publ} - не найден.")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
 #               pytest.fail()

def test_add_lock_publ(browser):
    add_lock_publ(browser)