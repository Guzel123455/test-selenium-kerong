# Строка Поиск в разделе BU платы

from test_func.test_func_search_plata_CU import search_plata_CU
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_search_plata_CU(browser):

    # авторизация
    authorization(browser)

    # поиск платы
    search_plata_CU(browser)