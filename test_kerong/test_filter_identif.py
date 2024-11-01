# фильтр в идентификаторы

from test_kerong.test_authorization import authorization
from browser_setup import browser
from test_func.test_func_filter_identif import filter_identif


def test_filter_identif(browser):

    # авторизация
    authorization(browser)

    # фильтры
    filter_identif(browser)