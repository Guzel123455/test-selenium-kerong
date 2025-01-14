# Платы. Фильтры в CU платах

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_plata.test_func_plata.test_func_filter_CU_plata import filter_CU_plata


def test_filter_CU_plata(browser):

    # авторизация
    authorization(browser)

    # фильтры
    filter_CU_plata(browser)