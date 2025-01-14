# Права доступа. Удалить всех пользователей

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_delete_all_user import delete_all_user


def test_delete_all_user(browser):

    authorization(browser)
    delete_all_user(browser)

