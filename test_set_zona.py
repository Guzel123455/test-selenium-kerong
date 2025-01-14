# Авторизация
# Добавить зону (приватная)
# Добавить зону (публичная)
# Добавить зону (корпоративная)
# Редактировать
# Поиск
# Фильтрация
# Печать данных


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_zona.test_func_zona.test_func_add_zone_private import add_zone_private
from test_zona.test_func_zona.test_func_add_zone_publ import add_zone_publ
from test_zona.test_func_zona.test_func_add_zone_corp import add_zone_corp
from test_zona.test_func_zona.test_func_edit_zone_publ import edit_zone_publ
from test_zona.test_func_zona.test_func_search_zona import search_zona
from test_zona.test_func_zona.test_func_filter_zona import filter_zona
from test_zona.test_func_zona.test_func_downloads_zona import downloads_zona
from termcolor import cprint



def test_set_zona(browser):

    cprint("Авторизация", "green")
    authorization(browser)
    print()

    cprint("Добавить зону (приватная)", "green")
    add_zone_private(browser)
    print()

    cprint("Добавить зону (публичная)", "green")
    add_zone_publ(browser)
    print()

    cprint("Добавить зону (корпоративная)", "green")
    add_zone_corp(browser)
    print()

    cprint("Редактировать", "green")
    edit_zone_publ(browser)
    print()

    cprint("Поиск", "green")
    search_zona(browser)
    print()

    cprint("Фильтрация", "green")
    filter_zona(browser)
    print()

    cprint("Печать данных", "green")
    downloads_zona(browser)