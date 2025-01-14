# Мониторинг. Зона. Фильтр - Свободные, Занятые, Все

from selenium.common import TimeoutException
from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
from config import name_zone_publ
from time import sleep


def filter_accident_lock_monitoring(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Мониторинг. Зона. Фильтр - Свободные / test_func_filter_free_lock_monitoring", "yellow")

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

    # свободные
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Аварийные']"))).click()
    print("Фильтр на 'Аварийные' ячейки")

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Применить']"))).click()

    # Получить отфильтрованные ячейки
    try:
        filtered_cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
        print(f"После фильтрации кол-во ячеек: {len(filtered_cells)}")

    except TimeoutException:
        print("Нет ячеек, соответствующих фильтру")
        # клик по фильтру
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()
        # сброс фильтра
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Сбросить']"))).click()
        return

    # Сбор информации о ячейках
    for cell in filtered_cells:

        # номер ячейки
        cell_number = cell.find_element(By.XPATH, ".//div[@class='text-container']").text
        # статус свободен
        free_status = cell.find_element(By.XPATH, ".//div[@class='free']").text if cell.find_elements(By.XPATH,".//div[@class='free']") else "Нет информации"
        # статус авария
        acc_status = cell.find_element(By.XPATH, ".//div[@class='failure']").text if cell.find_elements(By.XPATH,".//div[@class='failure']") else "Нет информации"

        # Определение статуса
        status = "Свободен" if free_status == "Свободен" else ("Авария" if acc_status == "Авария" else "Неизвестно")
        print(f"{cell_number}, {status}")

    # клик по фильтру
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()
    # сброс фильтра
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Сбросить']"))).click()


def filter_free_lock_monitoring(browser):
    wait = WebDriverWait(browser, 5)

    cprint("Мониторинг. Зона. Фильтр - Свободные, Занятые, Все / test_func_filter_monitoring", "yellow")

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

    # свободные
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Свободные']"))).click()
    print("Фильтр на 'Свободные' ячейки")

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Применить']"))).click()

    # Получить отфильтрованные ячейки
    try:
        filtered_cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
        print(f"После фильтрации кол-во ячеек: {len(filtered_cells)}")

    except TimeoutException:
        print("Нет ячеек, соответствующих фильтру")
        # клик по фильтру
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()
        # сброс фильтра
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Сбросить']"))).click()
        return

        # Сбор информации о ячейках
    for cell in filtered_cells:

        # номер ячейки
        cell_number = cell.find_element(By.XPATH, ".//div[@class='text-container']").text
        # статус свободен
        free_status = cell.find_element(By.XPATH, ".//div[@class='free']").text if cell.find_elements(By.XPATH,".//div[@class='free']") else "Нет информации"
        # статус авария
        acc_status = cell.find_element(By.XPATH, ".//div[@class='failure']").text if cell.find_elements(By.XPATH,".//div[@class='failure']") else "Нет информации"

        # Определение статуса
        status = "Свободен" if free_status == "Свободен" else ("Авария" if acc_status == "Авария" else "Неизвестно")
        print(f"{cell_number}, {status}")

    # клик по фильтру
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()
    # сброс фильтра
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Сбросить']"))).click()


def filter_rent_lock_monitoring(browser):
    wait = WebDriverWait(browser, 5)

    # фильтр
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()

    # выбрать статус ячейки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Выбрать статус ячейки']"))).click()

    # Занятые
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Занятые']"))).click()
    print("Фильтр на 'Занятые' ячейки")

    # применить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Применить']"))).click()

    # Получить отфильтрованные ячейки
    try:
        filtered_cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
        print(f"После фильтрации кол-во ячеек: {len(filtered_cells)}")

    except TimeoutException:
        print("Нет ячеек, соответствующих фильтру")
        # клик по фильтру
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()
        # сброс фильтра
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Сбросить']"))).click()
        return

        # Сбор информации о ячейках
    for cell in filtered_cells:
        # номер ячейки
        cell_number = cell.find_element(By.XPATH, ".//div[@class='text-container']").text
        # статус свободен
        rent_status = cell.find_element(By.XPATH, ".//div[@class='rent']").text if cell.find_elements(By.XPATH,
                                                                                                      ".//div[@class='rent']") else "Нет информации"

        # Определение статуса
        status = "Занят" if rent_status == "Занят" else "Нет информации"
        print(f"{cell_number}, {status}")

    # клик по фильтру
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()
    # сброс фильтра
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Сбросить']"))).click()

def filter_all_lock_monitoring(browser):
    wait = WebDriverWait(browser, 5)

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


def test_filter_accident_lock_monitoring(browser):
    filter_accident_lock_monitoring(browser)

def test_filter_free_lock_monitoring(browser):
    filter_free_lock_monitoring(browser)

def test_filter_rent_lock_monitoring(browser):
    filter_rent_lock_monitoring(browser)

def test_filter_all_lock_monitoring(browser):
    filter_all_lock_monitoring(browser)