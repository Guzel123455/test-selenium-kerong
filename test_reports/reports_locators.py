from selenium.webdriver.common.by import By

class Locator:

    # раздел отчеты
    REPORTS_BUTTON = (By.XPATH, "//button[text()='Отчеты']")

    EVENT_LOG_BUTTON = (By.XPATH, "//h2[text() = 'Журнал событий']")

    TABLE_BUTTON = (By.XPATH, "//button[text() = 'Таблица']")

    # фильтр
    FILTER_BUTTON = (By.XPATH, "//button[@class = 'filter-button']")

    # дата
    DATE_BUTTON = (By.XPATH, "//button[text() = 'Дата']")

    # дата начало
    BEGINNING_PERIOD = (By.XPATH, "(//input[@placeholder = 'DD.MM.YYYY'])[1]")

    # дата конец
    END_PERIOD = (By.XPATH, "(//input[@placeholder = 'DD.MM.YYYY'])[2]")

    # событие
    EVENT = (By.XPATH, "//button[text() = 'Событие']")

    # тип
    TYPE_OF_OPERATION = (By.XPATH, "//div[@id = 'Тип']")

    OPERATION_KR_BU = (By.XPATH, "//li[text() = 'Операция с KR-BU платой']")

    OPERATION_KR_CU = (By.XPATH, "//li[text() = 'Операция с KR-CU платой']")

    OPERATION_CELL = (By.XPATH, "//li[text() = 'Операция с ячейкой']")

    OPERATION_RENT = (By.XPATH, "//li[text() = 'Операция с арендой']")

    OPERATION_CLIENT = (By.XPATH, "//li[text() = 'Операция с клиентом']")

    APPLY_BUTTON = (By.XPATH, "//button[text() = 'Применить']")

    # колво строк
    COUNT_LINES = (By.XPATH, "//p[@class = 'MuiTablePagination-displayedRows css-1chpzqh']")

    RESET_BUTTON = (By.XPATH, "//button[text() = 'Сбросить']")

    # показывать по
    BUTTON_SHOW_BY = (By.XPATH, "//div[@class = 'MuiInputBase-root MuiInputBase-colorPrimary MuiTablePagination-input css-rmmij8']")
    # по 100
    BUTTON_100 = (By.XPATH, "//li[@data-value= '100']")










