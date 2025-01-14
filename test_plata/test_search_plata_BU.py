# Платы. Строка Поиска. BU платы

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_plata.test_func_plata.test_func_search_plata_BU import search_plata_BU



def test_search_plata_BU(browser):

    # авторизация
    authorization(browser)

    # поиск
    search_plata_BU(browser)