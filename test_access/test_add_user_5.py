# Права доступа. Добавить пользователя. User_5


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_add_user_5 import user_5


def test_user_5(browser):


    authorization(browser)
    user_5(browser)


