# Клиенты. Карточка клиента. Удалить доступ в корп зону

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_add_ident_in_client import add_ident_in_client
from test_client.test_func_client.test_func_access_corporate_zone import access_corporate_zone
from test_client.test_func_client.test_func_delete_access_corporate_zone import delete_access



def test_delete_ident(browser):

    # Вызов функции авторизации
    authorization(browser)

    # Добавить идентификатор в карточке Клиента
    add_ident_in_client(browser)
    print()

    # Добавить доступ
    access_corporate_zone(browser)
    print()

    # удаление доступа в корп зону
    delete_access(browser)