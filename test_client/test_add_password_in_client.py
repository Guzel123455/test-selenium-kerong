# Клиенты. Открыть карточку клиента. Пароль приложения

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_add_ident_in_client import add_ident_in_client
from test_client.test_func_client.test_func_add_password_in_client import add_password_in_client

def test_add_password_in_client(browser):

    # Авторизация
    authorization(browser)

    # Добавить идентификатор в карточке Клиента
    add_ident_in_client(browser)
    print()

    # Сгенерировать пароль
    add_password_in_client(browser)

