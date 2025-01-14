# Права доступа. Добавить пользователя, отредактировать.


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_edit_user import edit_user


def test_edit_user(browser):

    authorization(browser)
    edit_user(browser)
