# Права доступа. Активные / Неактивные пользователи

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_active_inactive_user import active_inactive_user


def test_active_inactive_user(browser):

    authorization(browser)
    active_inactive_user(browser)


