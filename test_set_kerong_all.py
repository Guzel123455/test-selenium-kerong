# Редактировать карточку
# Редактировать и синхронизировать данные
# Добавить соединение с kerong api
# Поиск
# Печать данных

from test_auth.test_authorization import authorization
from test_kerong_api.test_func_kerong_api.test_func_edit_kerong_api_not_synchr import edit_kerong_not_synchr
from test_kerong_api.test_func_kerong_api.test_func_edit_kerong_api_synchr import edit_kerong_synchr
from test_kerong_api.test_func_kerong_api.test_func_search_kerong_api import search_kerong
from test_kerong_api.test_func_kerong_api.test_func_downloads_kerong_api import downloads_kerong
from test_kerong_api.test_func_kerong_api.test_func_add_kerong_api import add_kerong
from browser_setup import browser
from termcolor import cprint


def test_add_kerong(browser):

    cprint("Авторизация", "green")
    authorization(browser)
    print()

    cprint("Редактировать и синхронизировать данные", "green")
    edit_kerong_synchr(browser)
    print()

    cprint("Редактировать карточку", "green")
    edit_kerong_not_synchr(browser)
    print()

    cprint("Добавить соединение с kerong api", "green")
    add_kerong(browser)
    print()

    cprint("Поиск", "green")
    search_kerong(browser)
    print()

    cprint("Загрузка файла", "green")
    downloads_kerong(browser)






