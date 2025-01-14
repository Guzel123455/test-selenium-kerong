# Авторизация
# Добавление и редактирование KR-BU
# Добавление и Редактирование KR-BU
# Поиск для BU платы
# Добавить KR-CU
# Редактирование KR-CU
# Поиск для CU платы
# Фильтрация: Тип платы, Номер в цепи, BU плата

import pytest
from browser_setup import browser
from test_auth.test_authorization import authorization
from test_plata.test_func_plata.test_func_edit_plata_BU import edit_card_BU
from test_plata.test_func_plata.test_func_edit_plata_CU import edit_card_CU
from test_plata.test_func_plata.test_func_search_plata_BU import search_plata_BU
from test_plata.test_func_plata.test_func_search_plata_CU import search_plata_CU
from test_plata.test_func_plata.test_func_filter_CU_plata import filter_CU_plata
from termcolor import cprint


class TestPlata:
    def test_plata_BU_CU(browser):

        cprint("Авторизация", "green")
        authorization(browser)
        print()

        cprint("Добавление и редактирование BU", "green")
        edit_card_BU(browser)
        print()

        cprint("Поиск для BU платы", "green")
        search_plata_BU(browser)
        print()

        cprint("Добавление и Редактирование CU", "green")
        edit_card_CU(browser)
        print()

        cprint("Поиск для CU платы", "green")
        search_plata_CU(browser)
        print()

        cprint("Фильтрация: Тип платы, Номер в цепи, BU плата", "green")
        filter_CU_plata(browser)
        print()

if __name__ == "__main__":
    pytest.main()




