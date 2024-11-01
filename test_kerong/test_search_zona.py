# Строка Поиск в разделе зоны

from test_func.test_func_search_zona import search_zona
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_search_zona(browser):

    # авторизация
    authorization(browser)

    # поиск платы
    search_zona(browser)