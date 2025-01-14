# Мониторинг. Зона. Фильтр - Все

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_filter_all_lock_monitoring import filter_all_lock_monitoring


def test_filter_all_lock_monitoring(browser):

    # авторизация
    authorization(browser)

    # фильтр все
    filter_all_lock_monitoring(browser)
