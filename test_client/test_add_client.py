# Клиенты. Создать карточку клиента

from test_client.test_func_client.test_func_add_client import add_client
from test_auth.test_authorization import authorization
from browser_setup import browser


def test_add_client(browser):

    # Вызов функции авторизации
    authorization(browser)

    # добавление клиента
    add_client(browser)


