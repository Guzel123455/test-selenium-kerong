# Строка Поиск в разделе Типы идентификаторы

from test_func.test_func_search_type_identif import search_type_identif
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_search_type_identif(browser):

    # авторизация
    authorization(browser)

    # поиск
    search_type_identif(browser)