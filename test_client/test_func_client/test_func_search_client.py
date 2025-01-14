# Клиенты. Строка Поиска: по телефону, имени, идентификатору

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import TimeoutException
from time import sleep
from termcolor import cprint


def search_client(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    cprint("Клиенты. Строка Поиска: по телефону, имени, идентификатору / test_func_search_client", "yellow")

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # данные первого клиента в списке
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'amount-sublime-container']")))
    # имя
    name = browser.find_element(By.CSS_SELECTOR, "td:nth-child(1) h4")
    name_txt = name.text
    # телефон
    mobile = browser.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
    mobile_txt = mobile.text
    mobile_txt = mobile_txt.replace('+', '')
    # идентификатор
    ident = browser.find_element(By.CSS_SELECTOR, "td:nth-child(3) h2")
    ident_txt = ident.text
    print(f"Выбран клиент: {name_txt}, {mobile_txt}, {ident_txt}")
    print()

    # поиск по имени
    search = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Поиск']")))
    search.send_keys(name_txt)
    sleep(1)
    print(f"Поиск по имени '{name_txt}'")
    found_count_total = 0
    while True:
        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        found_count = 0
        for row in rows:
            try:
                h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h4")
                h2_text = h2_element.text.strip()
                if h2_text == name_txt:
                    found_count += 1
                    actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                    sleep(0.1)
            except Exception:
                continue
        found_count_total += found_count
        print(f"Количество найденных строк по имени: {found_count_total}")
        print()

        next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
        if next_page.is_enabled() and next_page.is_displayed():
            next_page.click()
            sleep(0.2)
        else:
            break
    if found_count_total == 0:
        print(f"{ident_txt} - значение не найдено")


    # поиск по телефону
    search.send_keys(mobile_txt)
    sleep(1)
    print(f"Поиск по номеру '{mobile_txt}'")
    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        found_count = 0
        for row in rows:
            found_count += 1
            try:
                h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
                h2_text = h2_element.text.strip()
                if h2_text[1:] == mobile_txt:
                    actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                    sleep(0.1)
            except Exception:
                continue
        print(f"Количество найденных строк по телефону: {found_count}")
        print()
        if found_count == 0:
            print(f"{mobile_txt} - значение не найдено")
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            sleep(0.1)
    except TimeoutException:
        print("Нет значений")
    actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()


    # поиск по идентификатору
    if ident_txt == '':
        print("У клиента не выбран идентификатор")
    else:
        search.send_keys(ident_txt)
        sleep(1)
        print(f"Ищем по значению '{ident_txt}'")
        found_count_total = 0
        while True:
            WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
            rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
            found_count = 0
            for row in rows:
                try:
                    h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(3) h2")
                    h2_text_2 = h2_element.text.strip()
                    if h2_text_2 == ident_txt:
                        found_count += 1

                except Exception:
                    continue
            found_count_total += found_count
            print(f"Количество найденных строк по идентификатору на текущей странице: {found_count_total}")
            next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
            if next_page.is_enabled() and next_page.is_displayed():
                next_page.click()
                sleep(0.2)
            else:
                break
        actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()

        if found_count_total == 0:
            print(f"{ident_txt} - значение не найдено")

        # try:
        #
        #     next_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label = 'Go to next page']")))
        #
        #     WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
        #     rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
        #     found_count = 0
        #     for row in rows:
        #
        #         try:
        #             h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(3) h2")
        #             h2_text_2 = h2_element.text.strip()
        #             if next_page:
        #                 if h2_text_2 == ident_txt:
        #                     found_count += 1
        #                     # print(f"'{h2_text_2}' найден")
        #                     actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
        #                     sleep(0.1)
        #         except Exception:
        #             continue
        #     print(f"Количество найденных строк по идентификатору: {found_count}")
        #     if found_count == 0:
        #         print(f"{ident_txt} - значение не найдено")
        #         actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
        #         sleep(0.1)
        # except TimeoutException:
        #     print("Нет значений")

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

def test_search_client(browser):
    search_client(browser)