# Мониторинг. Открыть зону, получить список замков

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_open_zone_monitoring import open_monitor


def test_open_monitor(browser):

    # авторизация
    authorization(browser)

    # открытие зоны
    open_monitor(browser)