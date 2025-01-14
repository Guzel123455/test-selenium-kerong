# Авторизация
# Добавить Идентификатор
# Редактировать
# Создать и удалить идентификатор
# Удаление первого в списке идентификатора
# Поиск
# Фильтрация
# Печать данных


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_identif.test_func_identif.test_func_add_identif import add_ident
from test_identif.test_func_identif.test_func_edit_identif import edit_ident
from test_identif.test_func_identif.test_func_delete_identif import delete_ident
from test_identif.test_func_identif.test_func_delete_first_identif import delete_first_identif
from test_identif.test_func_identif.test_func_search_identif import search_identif
from test_identif.test_func_identif.test_func_filter_identif import filter_identif
from test_identif.test_func_identif.test_func_downloads_ident import downloads_ident
from termcolor import cprint


def test_set_ident(browser):

    cprint("Авторизация", "green")
    authorization(browser)
    print()

    cprint("Добавить идентификатор", "green")
    add_ident(browser)
    print()

    cprint("Редактировать идентификатор", "green")
    edit_ident(browser)
    print()

    cprint("Создать и удалить идентификатор", "green")
    delete_ident(browser)
    print()

    cprint("Удаление первого в списке идентификатора", "green")
    delete_first_identif(browser)
    print()

    cprint("Поиск", "green")
    search_identif(browser)
    print()

    cprint("Фильтрация", "green")
    filter_identif(browser)
    print()

    cprint("Печать данных", "green")
    downloads_ident(browser)









