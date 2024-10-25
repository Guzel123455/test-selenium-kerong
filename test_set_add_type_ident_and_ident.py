# создание карточки керонг, платы BU, CU, замков, ТИ, идентиф

from test_kerong.test_authorization import authorization
from test_func.test_func_add_type_identif import create_type_ident
from test_func.test_add_func_identif import create_ident
from browser_setup import browser

def test_add_type_ident_and_ident(browser):
    # авторизация
    authorization(browser)

    # создание типа идентиф
    create_type_ident(browser)

    # создание идентиф
    create_ident(browser)