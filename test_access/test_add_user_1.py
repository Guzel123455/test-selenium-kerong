# Права доступа. Добавить пользователя. User_1


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_add_user_1 import user_1


def test_user_1(browser):

    authorization(browser)
    user_1(browser)


