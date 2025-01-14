# Клиенты. Строка Поиска: по телефону, имени, идентификатору

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_search_client import search_client


def test_search_client (browser):

    # авторизация
    authorization(browser)

    # поиск
    search_client(browser)