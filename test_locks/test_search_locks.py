# Замки и ячейки. Строка Поиска

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_locks.test_func_locks.test_func_search_locks import search_locks


def test_search_locks(browser):

    # авторизация
    authorization(browser)

    # поиск
    search_locks(browser)