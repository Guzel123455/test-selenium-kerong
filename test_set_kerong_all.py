# авторизация и настройка керонг апи
# Редактировать карточку
# Редактировать и синхронизировать данные
# Поиск
# Печать данных

from test_kerong.test_authorization import authorization
from test_func.test_func_add_kerong_api import add_kerong
from test_func.test_func_edit_kerong_api_not_synchr import edit_kerong_not_synchr
from test_func.test_func_edit_kerong_api_synchr import edit_kerong_synchr
from test_func.test_func_search_kerong_api import search_kerong
from test_func.test_func_downloads_kerong_api import downloads_kerong
from browser_setup import browser

def test_add_kerong(browser):

    # авторизация
    authorization(browser)

    # Создание и редактирование карточки, синхронизация
    edit_kerong_synchr(browser)

    # создание карточки керонг, синхронизация
    add_kerong(browser)

    # создание карточки керонг, без синхронизации
    edit_kerong_not_synchr(browser)

    # Поиск
    search_kerong(browser)

    # Загрузка файла
    downloads_kerong(browser)




