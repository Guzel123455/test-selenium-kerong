# Мoниторинг - Зона. Открытие одной ячейки

from test_kerong.test_authorization import authorization
from test_func.test_func_open_lock_one_in_zona import open_lock_one
from browser_setup import browser


def test_open_lock_one(browser):

    #авторизация
    authorization(browser)

    # Открытие одной ячейки
    open_lock_one(browser)