# для поиска карточки в списке

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scroll_to_element(browser, element):
    # прокрутка к элементу
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.1)


def search_line(browser, expected_value):
    # Ждем, пока строки таблицы станут видимыми
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))

    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")

    # Проверяем каждую строку на наличие текста
    for row in rows:
        h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
        h2_text = h2_element.text.strip()

        # Прокрутка к элементу
        scroll_to_element(browser, h2_element)

        if h2_text == expected_value:
            print(f"{h2_text} - найден")
            return True

    # Если карточка не найдена, клик на следующую страницу
    try:
        next_page = browser.find_element(By.XPATH, "//button[@aria-label='Go to next page']")
        next_page.click()
        # рекурсивный вызов функции
        return search_line(browser, expected_value)
    except:
        print("Не найден на всех страницах.")
        return False
