# Строка Поиск в разделе идентификаторы

from test_func.test_func_search_identif import search_identif
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_search_type_identif(browser):

    # авторизация
    authorization(browser)

    # поиск
    search_identif(browser)