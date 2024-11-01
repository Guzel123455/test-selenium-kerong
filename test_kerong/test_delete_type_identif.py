# удаление Типа идентиф

from test_func.test_func_delete_type_identif import delete_type_ident
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_delete_type_ident(browser):

    # авторизация
    authorization(browser)

    # удаление
    delete_type_ident(browser)