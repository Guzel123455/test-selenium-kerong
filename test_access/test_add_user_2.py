# Права доступа. Добавить пользователя. User_2


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_add_user_2 import user_2


def test_user_2(browser):

    authorization(browser)
    user_2(browser)


