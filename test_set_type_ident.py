# Авторизация
# Добавить Тип идентификатора
# Редактировать
# Создать и удалить тип идентификатора
# Удаление первого в списке типа идентификатора
# Поиск
# Печать данных


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_type_identif.test_func_type_identif.test_func_add_type_identif import add_type_ident
from test_type_identif.test_func_type_identif.test_func_edit_type_identif import edit_type_ident
from test_type_identif.test_func_type_identif.test_func_delete_type_identif import delete_type_ident
from test_type_identif.test_func_type_identif.test_func_delete_first_type_identif import delete_first_type_identif
from test_type_identif.test_func_type_identif.test_func_search_type_identif import search_type_identif
from test_type_identif.test_func_type_identif.test_func_downloads_type_ident import downloads_type_ident
from termcolor import cprint


def test_set_type_ident(browser):

    cprint("Авторизация", "green")
    authorization(browser)
    print()

    cprint("Добавить Тип идентификатора", "green")
    add_type_ident(browser)
    print()

    cprint("Редактировать", "green")
    edit_type_ident(browser)
    print()

    cprint("Создать и удалить тип идентификатора", "green")
    delete_type_ident(browser)
    print()

    cprint("Поиск", "green")
    search_type_identif(browser)
    print()

    cprint("Удаление первого в списке типа идентификатора", "green")
    delete_first_type_identif(browser)
    print()

    cprint("Печать данных", "green")
    downloads_type_ident(browser)





