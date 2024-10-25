# Мoниторинг - Зона. Открытие всех ячеек

from test_kerong.test_authorization import authorization
from test_func.test_func_open_all_lock_in_zona import open_lock_all
from browser_setup import browser


def test_open_lock(browser):

    # авторизация
    authorization(browser)

    # Открытие всех ячеек
    open_lock_all(browser)