# Права доступа. Удалить пользователя

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_delete_user import delete_user


def test_delete_user(browser):

    authorization(browser)
    delete_user(browser)


