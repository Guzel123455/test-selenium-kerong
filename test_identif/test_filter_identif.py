# Идентификаторы. Фильтр

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_identif.test_func_identif.test_func_filter_identif import filter_identif


def test_filter_identif(browser):

    # авторизация
    authorization(browser)

    # фильтры
    filter_identif(browser)