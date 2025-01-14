# Идентификатор. Создание карточки

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_identif.test_func_identif.test_func_add_identif import add_ident


def test_add_ident(browser):

    # авторизация
    authorization(browser)

    # создание идентиф
    add_ident(browser)
