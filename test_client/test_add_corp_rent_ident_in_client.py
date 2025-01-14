# Клиенты. Открыть карточку клиента. Добавить доступ к ячейкам на корп.зону , по идентификатору

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_add_ident_in_client import add_ident_in_client
from test_client.test_func_client.test_func_access_corporate_zone import access_corporate_zone
from test_client.test_func_client.test_func_add_corp_rent_ident_in_client import add_corp_rent_ident_in_client


def test_add_corp_rent_ident_in_client(browser):

    # Авторизация
    authorization(browser)

    # Добавить идентификатор в карточке Клиента
    add_ident_in_client(browser)
    print()

    # Добавить доступ к зонам
    access_corporate_zone(browser)
    print()

    # добавить к ячейкам
    add_corp_rent_ident_in_client(browser)
