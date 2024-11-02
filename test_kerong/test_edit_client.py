# редактирование карточки клиента

from test_kerong.test_authorization import authorization
from browser_setup import browser
from test_func.test_func_edit_client import edit_client


def test_edit_client(browser):

    # Вызов функции авторизации
    authorization(browser)

    # редактирование клиента
    edit_client(browser)
