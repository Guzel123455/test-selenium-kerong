# создание, поиск, редактирование CU платы

from test_kerong.test_authorization import authorization
from test_func.test_func_add_plata_CU import add_card_CU
from test_func.test_func_edit_plata_CU import edit_card_CU
from test_func.test_func_search_plata_CU import search_plata_CU
from browser_setup import browser

def test_add_and_edit_pata_CU(browser):

    # авторизация
    authorization(browser)

    # создание CU
    add_card_CU(browser)

    # Поиск платы
    search_plata_CU(browser)

    # редактирование CU платы
    edit_card_CU(browser)



