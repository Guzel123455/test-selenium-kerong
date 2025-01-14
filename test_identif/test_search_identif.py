# Идентификаторы. Строка Поиска

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_identif.test_func_identif.test_func_search_identif import search_identif


def test_search_type_identif(browser):

    # авторизация
    authorization(browser)

    # поиск
    search_identif(browser)