# добавление замков, поиск, удаление

import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import new_name_lock, name_BU_text, name_CU_text, name_zone_publ, num_from_publ, num_to_publ, new_count_lock, new_star_num_plata, new_stop_num_plata, new_count_lock_plata, new_start_num_lock, new_stop_num_lock
from browser_setup import browser
from selenium.webdriver.common.action_chains import ActionChains

def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.1)

def add_search_delete_locks(browser):
    wait = WebDriverWait(browser, 20)
    actions = ActionChains(browser)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик на замки и ячейки
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'settings-item'])[3]"))).click()

    # Клик на Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'UIbutton']"))).click()

    # Выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'demo-simple-select-helper'])[1]"))).click()
    x = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{name_zone_publ} [{num_from_publ}-{num_to_publ}]')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", x)
    x.click()

    # Ввести наименование
    name_lock = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name_lock.send_keys(new_name_lock)

    # Стартовый номер
    start_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[3]")))
    start_num.send_keys(Keys.CONTROL, "a")
    start_num.send_keys(new_start_num_lock)

    # Конечный номер
    stop_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[4]")))
    stop_num.send_keys(Keys.CONTROL, "a")
    stop_num.send_keys(new_stop_num_lock)

    # Колво ячеек
    count_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[5]")))
    count_num.send_keys(Keys.CONTROL, "a")
    count_num.send_keys(new_count_lock)

    # Выбрать BU плату
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'demo-simple-select-helper'])[2]"))).click()
    b = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{name_BU_text}')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", b)
    browser.execute_script("arguments[0].click();", b)

    # Выбрать CU плату
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'demo-simple-select-helper'])[3]"))).click()
    c = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{name_CU_text}')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", c)
    browser.execute_script("arguments[0].click();", c)

    # Стартовый номер на плате
    start_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[7]")))
    start_num.send_keys(Keys.CONTROL, "a")
    start_num.send_keys(new_star_num_plata)

    # Конечный номер на плате
    stop_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[8]")))
    stop_num.send_keys(Keys.CONTROL, "a")
    stop_num.send_keys(new_stop_num_plata)

    # Колво плате
    count_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[9]")))
    count_num.send_keys(Keys.CONTROL, "a")
    count_num.send_keys(new_count_lock_plata)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    time.sleep(0.2)
    print("Набор замков создан")

    # строка поиска
    searc = wait.until(EC.element_to_be_clickable((By.XPATH, "// input[@id = 'outlined-basic']")))
    searc.send_keys(new_name_lock)
    print(f"Искомое значение '{new_name_lock}'")
    time.sleep(1)

    # поиск
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    for row in rows:
        h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
        h2_text = h2_element.text.strip()

        if h2_text == new_name_lock:
            print(f"'{h2_text}' найден")
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            time.sleep(0.3)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='MuiBox-root css-0']"))).click()
            print(f"'{new_name_lock}' - удален")
            return True
        else:
            print(f"Значение не найдено")
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            time.sleep(0.1)

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
 #               pytest.fail()

def test_add_search_delete_locks(browser):
    add_search_delete_locks(browser)