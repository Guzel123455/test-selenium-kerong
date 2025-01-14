# Права доступа. Добавить пользователя. User_6


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_add_user_6 import user_6


def test_user_6(browser):


    authorization(browser)
    user_6(browser)


