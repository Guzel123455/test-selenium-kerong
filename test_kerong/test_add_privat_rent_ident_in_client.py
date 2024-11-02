# Добавить доступ к ячейкам в карточке клиента

from test_func.test_func_add_privat_rent_ident_in_client import add_privat_rent_ident_in_client
from test_kerong.test_authorization import authorization
from browser_setup import browser

def test_add_privat_ident_rent_in_client(browser):

    # Авторизация
    authorization(browser)

    # добавить доступ
    add_privat_rent_ident_in_client(browser)

