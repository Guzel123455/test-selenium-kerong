# для поиска клиента

from selenium.webdriver.common.by import By
import time

def search_phone(browser, expected_value):
    flag = False
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

    # Проверяем каждую строку в таблице
    for row in rows:

        # Получаем номер телефона
        phone = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2")
        h2_phone = phone.text

        # Проверяем значение h4
        if h2_phone == expected_value:
            print("Значение соответствует:", h2_phone)
            return True

        # Если клиент не найден, пытаемся перейти на следующую страницу
    if not flag:
        try:
            next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
            next_page.click()
            time.sleep(1)
            # Рекурсивно вызываем функцию для новой страницы
            return search_phone(browser, expected_value)
        except:
            print("Не найден на всех страницах.")
            return False


