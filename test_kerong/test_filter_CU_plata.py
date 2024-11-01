# фильтры в CU платах

from test_kerong.test_authorization import authorization
from browser_setup import browser
from test_func.test_func_filter_CU_plata import filter_CU_plata


def test_filter_CU_plata(browser):

    # авторизация
    authorization(browser)

    # фильтры
    filter_CU_plata(browser)