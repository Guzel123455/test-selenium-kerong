# создание, поиск, редактирование CU платы

from test_kerong.test_authorization import authorization
from test_func.test_func_add_plata_CU import create_and_check_card_CU
from test_func.test_func_edit_plata_CU import edit_card_CU
from browser_setup import browser

def test_add_and_edit_pata_CU(browser):

    # авторизация
    authorization(browser)

    # создание CU
    create_and_check_card_CU(browser)

    # Поиск платы


    # редактирование CU платы
    edit_card_CU(browser)



