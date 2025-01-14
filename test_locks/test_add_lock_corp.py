# Замки и ячейки. Создание набора замков для корп зоны

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_locks.test_func_locks.test_func_add_lock_corp import add_lock_corp


def test_add_lock_corp(browser):

    #авторизация
    authorization(browser)

    #создание замков
    add_lock_corp(browser)