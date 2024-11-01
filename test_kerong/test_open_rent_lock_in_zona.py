# Мoниторинг - Зона. Открытие занятых ячеек

from test_kerong.test_authorization import authorization
from test_func.test_func_open_rent_lock_in_zona import open_lock_rent
from browser_setup import browser


def test_open_lock_rent(browser):

    #авторизация
    authorization(browser)

    # Открытие занятых ячейки
    open_lock_rent(browser)