# Мониторинг. Открыть ячейку

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_open_lock import open_lock


def test_open_lock(browser):

    # авторизация
    authorization(browser)

    # открытие ячейки
    open_lock(browser)
