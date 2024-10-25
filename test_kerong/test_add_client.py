# Добавление клиента и проверка наличия карточки

from test_func.test_func_add_client import client_find
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_add_client(browser):

    # Вызов функции авторизации
    authorization(browser)

    # вызов функции добавления клиента
    client_find(browser)


