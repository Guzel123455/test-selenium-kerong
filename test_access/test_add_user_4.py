# Права доступа. Добавить пользователя. User_4


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_add_user_4 import user_4


def test_user_4(browser):

    authorization(browser)
    user_4(browser)


