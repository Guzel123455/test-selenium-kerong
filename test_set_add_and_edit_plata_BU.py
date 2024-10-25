# создание, поиск, редактирование BU платы

from test_kerong.test_authorization import authorization
from test_func.test_func_add_plata_BU import create_and_check_card_BU
from test_func.test_func_edit_plata_BU import edit_card_BU
from browser_setup import browser


def test_add_and_edit_pata_BU(browser):

    # авторизация
    authorization(browser)

    # создание BU
    create_and_check_card_BU(browser)

    # Поиск платы

    # редактирование BU платы
    edit_card_BU(browser)



