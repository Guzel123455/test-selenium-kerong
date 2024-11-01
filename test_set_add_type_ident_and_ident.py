# Создание и редактирование типа идентификатора, идентификатора

from test_kerong.test_authorization import authorization
from test_func.test_func_edit_type_identif import edit_type_ident
from test_func.test_func_edit_identif import edit_ident
from test_func.test_func_search_identif import search_identif
from test_func.test_func_search_type_identif import search_type_identif
from test_func.test_func_filter_identif import filter_identif
from test_func.test_func_delete_identif import delete_ident
from test_func.test_func_delete_type_identif import delete_type_ident
from test_func.test_func_downloads_ident import downloads_ident
from test_func.test_func_downloads_type_ident import downloads_type_ident
from browser_setup import browser

def test_add_type_ident_and_ident(browser):

    print()
    # авторизация
    authorization(browser)

    # создание и редактирование типа идентиф
    edit_type_ident(browser)
    print()

    # поиск типа идентиф
    search_type_identif(browser)
    print()

    # создание и редактирование идентиф
    edit_ident(browser)
    print()

    # поиск идентиф
    search_identif(browser)
    print()

    # фильтр
    filter_identif(browser)
    print()

    # удаление идентиф
    delete_ident(browser)
    print()

    # удаление типа идентиф
    delete_type_ident(browser)
    print()

    # печать в ТИ
    downloads_type_ident(browser)
    print()

    # печать идентиф
    downloads_ident(browser)
    print()




