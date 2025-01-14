# добавление замков (в публичную зону) и проверка наличия

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_locks.test_func_locks.test_func_add_lock_publ import add_lock_publ


def test_add_lock_publ(browser):

    #авторизация
    authorization(browser)

    #создание замков
    add_lock_publ(browser)