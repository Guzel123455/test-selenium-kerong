# Мoниторинг. Зона. Открыть - одну ячейку

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_open_lock_one_in_zona import open_lock_one


def test_open_lock_one(browser):

    #авторизация
    authorization(browser)

    # Открытие одной ячейки
    open_lock_one(browser)