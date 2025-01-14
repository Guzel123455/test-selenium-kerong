# Мониторинг. Зона. Фильтр - Занятые

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_filter_rent_lock_monitoring import filter_rent_lock_monitoring


def test_filter_rent_lock_monitoring(browser):

    # авторизация
    authorization(browser)

    # фильтр на занятые ячейки
    filter_rent_lock_monitoring(browser)