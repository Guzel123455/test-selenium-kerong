# Платы. Создание платы CU

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_plata.test_func_plata.test_func_add_plata_CU import add_card_CU


def test_add_card_CU(browser):

    #авторизация
    authorization(browser)

    #создание CU платы
    add_card_CU(browser)