# Отчеты. Журнал событий. Таблица. Фильтр на Операция с арендой

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from test_reports.reports_locators import Locator


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)

def event_log_filter_rent(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Отчеты. Журнал событий. Таблица. Фильтр на Операция с арендой / test_func_event_log_filter_RENT", "yellow")

    # отчеты
    wait.until(EC.visibility_of_element_located((Locator.REPORTS_BUTTON))).click()

    # журнал событий
    wait.until(EC.visibility_of_element_located((Locator.EVENT_LOG_BUTTON))).click()

    # таблица
    wait.until(EC.visibility_of_element_located((Locator.TABLE_BUTTON))).click()

    # фильтр
    wait.until(EC.visibility_of_element_located(Locator.FILTER_BUTTON)).click()

    # событие
    wait.until(EC.visibility_of_element_located(Locator.EVENT)).click()

    # тип операции
    wait.until(EC.visibility_of_element_located(Locator.TYPE_OF_OPERATION)).click()


    # Операция с арендой
    a = wait.until(EC.visibility_of_element_located(Locator.OPERATION_RENT))
    scroll_to_element(browser, a)
    a.click()

    # применить
    wait.until(EC.visibility_of_element_located(Locator.APPLY_BUTTON)).click()

    # показывать по
    wait.until(EC.visibility_of_element_located(Locator.BUTTON_SHOW_BY)).click()

    # по 100
    wait.until(EC.visibility_of_element_located(Locator.BUTTON_100)).click()
    sleep(0.2)

    # колво записей
    line = wait.until(EC.visibility_of_element_located(Locator.COUNT_LINES))
    line_text = line.text
    print(f"Кол-во записей после фильтрации {line_text}")

    while True:
        try:
            WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
            rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
            for row in rows:
                h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(3) h2")
                h2_text = h2_element.text

                # Прокрутка к элементу
                scroll_to_element(browser, h2_element)

                if h2_text != "Аренда":
                    raise AssertionError(f"Несоответствие на странице: {h2_text}")

            # Переход на следующую страницу
            next_button = browser.find_element(By.XPATH, "//button[@aria-label='Go to next page']")
            if "disabled" in next_button.get_attribute("class"):
                print("На всех страницах 'Тип операции' соответствует 'Операция с арендой' ")
                break  # Выход, если последняя страница
            next_button.click()

        except TimeoutException:
            print("Нет значений")
            break


def test_event_log_filter_rent(browser):
    event_log_filter_rent(browser)



