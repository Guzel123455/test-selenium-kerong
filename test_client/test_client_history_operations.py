# Клиенты. Карточка клиента. История операций аренды

from test_client.test_func_client.test_func_client_history_operations import choose_indent_in_client, client_history_operation
from test_auth.test_authorization import authorization
from browser_setup import browser


def test_client_history_operation(browser):

    authorization(browser)
    choose_indent_in_client(browser)
    client_history_operation(browser)


