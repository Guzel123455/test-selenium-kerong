# Добавление и редактирование KR-BU
# Добавление и Редактирование KR-BU
# Поиск для BU платы
# Добавить KR-CU
# Редактирование KR-CU
# Поиск для CU платы
# Фильтрация: Тип платы, Номер в цепи, BU плата

from test_kerong.test_authorization import authorization
from browser_setup import browser
from test_func.test_func_edit_plata_BU import edit_card_BU
from test_func.test_func_edit_plata_CU import edit_card_CU
from test_func.test_func_search_plata_BU import search_plata_BU
from test_func.test_func_search_plata_CU import search_plata_CU
from test_func.test_func_filter_CU_plata import filter_CU_plata

def test_plata_BU_CU(browser):
    print()
    # авторизация
    authorization(browser)

    # Добавление и редактирование KR-BU
    edit_card_BU(browser)
    print()

    # Поиск для BU платы
    search_plata_BU(browser)
    print()

    # Добавление и Редактирование KR-BU
    edit_card_CU(browser)
    print()

    # Поиск для CU платы
    search_plata_CU(browser)
    print()

    # Фильтрация: Тип платы, Номер в цепи, BU плата
    filter_CU_plata(browser)
    print()







