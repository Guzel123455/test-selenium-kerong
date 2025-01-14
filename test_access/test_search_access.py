# Права доступа. Поле поиск


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_search_access import search_access


def test_search_access(browser):

    authorization(browser)
    search_access(browser)

