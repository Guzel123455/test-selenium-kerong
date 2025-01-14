# Клиенты. Карточка клиента. Удалить идентификатор

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_choose_indent_in_client_1 import choose_indent_in_client
from test_client.test_func_client.test_func_delete_ident_in_client import delete_ident_in_client

def test_delete_ident(browser):

    #авторизация
    authorization(browser)

    # добавление идентификатора
    choose_indent_in_client(browser)

    # удаление
    delete_ident_in_client(browser)