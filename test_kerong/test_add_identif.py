# добавление идентиф и проверка наличия карточки

from test_kerong.test_authorization import authorization
from test_func.test_func_add_identif import add_ident
from browser_setup import browser



def test_add_ident(browser):

    # авторизация
    authorization(browser)

    # создание идентиф
    add_ident(browser)
