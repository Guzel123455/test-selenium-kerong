# Клиенты. Редактирование карточки клиента

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_edit_client import edit_client


def test_edit_client(browser):

    # Вызов функции авторизации
    authorization(browser)

    # редактирование клиента
    edit_client(browser)
