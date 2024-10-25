# открыть ячейку со стартовой страници мониторинга

from test_kerong.test_authorization import authorization
from test_func.test_func_open_lock import open_lock
from browser_setup import browser


def test_open_lock(browser):

    # авторизация
    authorization(browser)

    # открытие ячейки
    open_lock(browser)
