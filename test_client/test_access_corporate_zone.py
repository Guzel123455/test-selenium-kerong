# Клиенты. Открыть карточку клиента. Добавить доступ в корп зону

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_add_ident_in_client import add_ident_in_client
from test_client.test_func_client.test_func_access_corporate_zone import access_corporate_zone

def test_access_corporate_zone(browser):

    # Вызов функции авторизации
    authorization(browser)

    # Добавить идентификатор в карточке Клиента
    add_ident_in_client (browser)

    # Добавить доступ
    access_corporate_zone(browser)


