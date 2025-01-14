# для поиска клиента

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def search_phone(browser, expected_value):
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

    # Проверяем каждую строку в таблице
    for row in rows:

        # Получаем номер телефона
        phone = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) h2").text

        # Проверяем значение h4
        if phone == expected_value:
            print(f"Найден '{phone}'")
            return True

    # Если клиент не найден, переход на след страницу
    try:
        next_page = browser.find_element(By.XPATH, "//button[@aria-label = 'Go to next page']")
        next_page.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tbody tr")))
        time.sleep(0.2)
            # Рекурсивно вызываем функцию для новой страницы
        return search_phone(browser, expected_value)
    except:
        print("Не найден на всех страницах")
        return False


