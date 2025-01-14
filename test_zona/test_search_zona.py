# Зоны. Строка Поиска

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_zona.test_func_zona.test_func_search_zona import search_zona



def test_search_zona(browser):

    # авторизация
    authorization(browser)

    # поиск
    search_zona(browser)