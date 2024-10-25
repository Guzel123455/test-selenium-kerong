# добавление и поиск платы BU

from test_func.test_func_add_plata_BU import create_and_check_card_BU
from test_func.test_func_add_plata_CU import create_and_check_card_CU
from test_kerong.test_authorization import authorization
from browser_setup import browser

def test_add_plata_BU_CU(browser):

    #авторизация
    authorization(browser)

    #создание BU
    create_and_check_card_BU(browser)

    #создание CU
    create_and_check_card_CU(browser)
