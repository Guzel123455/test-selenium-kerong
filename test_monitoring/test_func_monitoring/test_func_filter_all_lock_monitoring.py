# Мониторинг. Зона. Фильтр - Все

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import name_zone_publ
from time import sleep
from termcolor import cprint

def filter_all_lock_monitoring(browser):
    wait = WebDriverWait(browser, 5)

    cprint("Мониторинг. Зона. Фильтр - Все / test_func_filter_all_lock_monitoring", "yellow")

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()
    sleep(1)

    # Все ячейки
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"В зоне '{name_zone_publ}' кол-во ячеек: {len(cells)}")

    # фильтр
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()

    # выбрать статус ячейки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать статус ячейки']"))).click()

    # Занятые
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Все']"))).click()
    print("Фильтр на 'Все' ячейки")

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Применить']"))).click()

    filtered_cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"После фильтрации кол-во ячеек: {len(filtered_cells)}")

    # клик по фильтру
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()
    # сброс фильтра
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Сбросить']"))).click()


def test_filter_all_lock_monitoring(browser):
    filter_all_lock_monitoring(browser)