# Клиенты. Карточка клиента. Выбрать идентификатор

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_choose_indent_in_client import MyClass


def test_choose_indent_in_client(browser):

    authorization(browser)

    my_client = MyClass()
    my_client.add_client(browser)
    my_client.choose_indent_in_client(browser)

