# Поиск клиента по телефону, имени, идентификатору

from test_func.test_func_search_client import search_client
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_search_client (browser):

    # авторизация
    authorization(browser)

    # поиск
    search_client(browser)