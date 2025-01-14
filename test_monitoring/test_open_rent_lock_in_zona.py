# Мoниторинг. Зона. Открыть - По статусу - Занятые ячейки

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_open_rent_lock_in_zona import open_lock_rent


def test_open_lock_rent(browser):

    #авторизация
    authorization(browser)

    # Открытие занятых ячейки
    open_lock_rent(browser)