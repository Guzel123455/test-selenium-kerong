# Мoниторинг - Зона. Открытие одной, нескольких, занятых, свободных ячейки

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_open_lock_one_in_zona import open_lock_one
from test_func.test_func_open_some_lock_in_zona import open_lock_some
from test_func.test_func_open_rent_lock_in_zona import open_lock_rent
from test_func.test_func_open_free_lock_in_zona import open_lock_free



def test_open_lock(browser):

    #авторизация
    authorization(browser)

    # Открытие одной ячейки
    open_lock_one(browser)

    # Открытие нескольких ячейки
    open_lock_some(browser)

    # Открытие занятых ячейки
    open_lock_rent(browser)

    # Открытие свободных ячейки
    open_lock_free(browser)
