# Права доступа. Добавить пользователя. User_3


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_add_user_3 import user_3


def test_user_3(browser):

    authorization(browser)
    user_3(browser)


