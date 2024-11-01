# Строка Поиск в разделе Замки и ячейки

from test_func.test_func_search_locks import search_locks
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_search_locks(browser):

    # авторизация
    authorization(browser)

    # поиск платы
    search_locks(browser)