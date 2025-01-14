# Отчеты. Журнал событий. Таблица. Фильтр по дате

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

def event_log_filter_date(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Отчеты. Журнал событий. Таблица. Фильтр по дате / test_func_event_log_filter_DATE", "yellow")

    # отчеты
    wait.until(EC.visibility_of_element_located((Locator.REPORTS_BUTTON))).click()

    # журнал событий
    wait.until(EC.visibility_of_element_located((Locator.EVENT_LOG_BUTTON))).click()

    # таблица
    wait.until(EC.visibility_of_element_located((Locator.TABLE_BUTTON))).click()
    sleep(0.2)

    # дата в первой строке
    date_element = browser.find_element(By.CSS_SELECTOR, 'tr.MuiTableRow-root td:nth-child(1) h2')
    # Получаем текст и удаляем лишние пробелы
    date_time = date_element.text.strip()
    # Извлекаем только дату (до символа '|')
    date_only = date_time.split('|')[0].strip()
    print(f"Поиск по дате {date_only}")

    # фильтр
    wait.until(EC.visibility_of_element_located(Locator.FILTER_BUTTON)).click()

    # начало периода
    start = wait.until(EC.visibility_of_element_located(Locator.BEGINNING_PERIOD))
    start.click()
    start.send_keys(date_only)

    # конец периода
    stop = wait.until(EC.visibility_of_element_located(Locator.END_PERIOD))
    stop.click()
    stop.send_keys(date_only)

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

    date = True
    while True:
        try:
            WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
            rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
            for row in rows:
                h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
                date_time1 = h2_element.text.strip()
                date_only1 = date_time1.split('|')[0].strip()

                # Прокрутка к элементу
                scroll_to_element(browser, h2_element)

                if date_only1 != date_only:
                    print(f"Дата не совпадает: {date_only1}")
                    date = False

            # Переход на следующую страницу
            next_button = browser.find_element(By.XPATH, "//button[@aria-label='Go to next page']")
            if "disabled" in next_button.get_attribute("class"):
                break  # Выход, если последняя страница
            next_button.click()

        except TimeoutException:
            print("Нет значений")
            break

    # Проверяем итоговый результат
    if not date:
        raise AssertionError("Даты не совпадают на всех страницах")
    else:
        print("Даты совпадают")

def test_event_log_filter_date(browser):
    event_log_filter_date(browser)