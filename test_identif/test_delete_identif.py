#  Идентификаторы. Создание и удаление идентификатора

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_identif.test_func_identif.test_func_delete_identif import delete_ident


def test_delete_ident(browser):

    #авторизация
    authorization(browser)

    # удаление
    delete_ident(browser)