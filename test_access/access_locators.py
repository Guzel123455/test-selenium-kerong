from selenium.webdriver.common.by import By


class Locator:

    # настройки
    SETTINGS_BUTTON = (By.XPATH, "(//button[text() = 'Настройки'])[1]")

    # раздел права доступа
    ACCESS_BUTTON = (By.XPATH, "//h2[text() = 'Права доступа']")

    # поиск
    SEARCH = (By.XPATH, "//input[@id = 'Поиск']")

    # неактивные пользователи
    INACTIVE_USER = (By.XPATH, "//span[@aria-label = 'Показывать неактивных пользователей']")

    # добавить пользователя
    ADD_USER = (By.XPATH, "//button[text() = 'Добавить пользователя']")

    # фамилия
    SURNAME = (By.XPATH, "//input[@id = 'Фамилия*']")
    NEW_SURNAME = (By.XPATH, "//input[@id = 'Фамилия']")

    # ИМЯ
    NAME = (By.XPATH, "//input[@id = 'Имя*']")
    NEW_NAME = (By.XPATH, "//input[@id = 'Имя']")

    # логин
    LOGIN = (By.XPATH, "//input[@id = 'Логин*']")
    NEW_LOGIN = (By.XPATH, "//input[@id = 'Логин']")

    # пароль
    PASSWORD = (By.XPATH, "//input[@id = 'Пароль*']")
    NEW_PASS = (By.XPATH, "//input[@id = 'Новый пароль']")

    # подтверждение пароля
    DOUBLE_PASS = (By.XPATH, "//input[@id = 'Подтверждение пароля*']")
    NEW_DOUBLE_PASS = (By.XPATH, "//input[@id = 'Подтверждение пароля']")


    # Вкладка Права доступа
    ACCESS = (By.XPATH, "//button[text() = 'Права доступа']")

    # галочка админ
    ADMIN = (By.XPATH, "//div[@id = 'Администратор']")
    # админ - нет
    NO_ADMIN = (By.XPATH, "//li[text() = 'Нет']")

    # клиенты
    CLIENT = (By.XPATH, "//div[@id = 'Клиенты']")
    # чтение
    READ = (By.XPATH, "//li[text() = 'Чтение']")
    # Запись/чтение
    RECORD_READ = (By.XPATH, "//li[text() = 'Запись/чтение']")
    # Отчеты
    REPORTS = (By.XPATH, "//div[@id = 'Отчеты']")
    # отчеты -есть
    REPORTS_YES = (By.XPATH, "//li[text() = 'Есть']")
    # аренда
    RENT = (By.XPATH, "//div[@id = 'Аренда']")
    # чтение/запись
    RENT_RECORD = (By.XPATH, "//li[text() = 'Чтение/Запись']")
    # открытие ячейки
    OPEN_LOCK = (By.XPATH, "//div[@id = 'Открытие ячейки']")

    # сохранить
    SAVE_BUTTON = (By.XPATH, "//button[text() = 'Сохранить']")

    # выйти из учетки admin
    LOG_OUT = (By.XPATH, "//button[@id= 'fade-button']")
    LOG_OUT_2 = (By.XPATH, "//div[text()= ' Выйти из аккаунта']")

    # ВВЕCТИ ЛОГИН
    INPUT_LOGIN = (By.XPATH, "//input[@id='Логин']")
    # ВВЕСТИ ПАРОЛЬ
    INPUT_PASS = (By.XPATH, "//input[@id='Пароль']")

    # войти
    LOG_IN = (By.XPATH, "//button[@class= 'UIbutton']")

    # редактировать
    EDIT_BUTTON = (By.XPATH, "//button[text()='Редактировать']")
    # удалить
    DELETE = (By.XPATH, "//button[text()='Удалить']")
    # удалть пользователя
    DELETE_USER = (By.XPATH, "//button[text()='Удалить пользователя']")

    # колво строк
    COUNT_LINES = (By.XPATH, "//p[@class = 'MuiTablePagination-displayedRows css-1chpzqh']")













