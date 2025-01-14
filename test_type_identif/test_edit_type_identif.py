# Идентификаторы. Добавление идентиф и редактирование

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_type_identif.test_func_type_identif.test_func_edit_type_identif import edit_type_ident


def test_edit_type_ident(browser):

    #авторизация
    authorization(browser)

    #создание и редактирование типа идентиф
    edit_type_ident(browser)