# Мониторинг. Открыть зону, получить список замков

from test_func.test_func_open_monitoring import open_monitor
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_open_zone(browser):

    # авторизация
    authorization(browser)

    # открытие зоны
    open_monitor(browser)