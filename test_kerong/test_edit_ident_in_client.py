# Добавить идентификатор в карточке Клиента

from test_func.test_func_edit_ident_in_client import edit_ident_in_client
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_func_edit_ident_in_client(browser):

    # Авторизация
    authorization(browser)

    # Выбрать идентификатор в карточке Клиента
    edit_ident_in_client(browser)

