# авторизация и настройка керонг апи
# Редактировать карточку
# Редактировать и синхронизировать данные
# Поиск
# Печать данных

import pytest
from test_kerong.test_authorization import authorization
from test_func.test_func_add_kerong_api import auth_kerong
from test_func.test_func_edit_kerong_api_not_synchr import edit_kerong
from test_func.test_func_edit_kerong_api_synchr import edit_kerong_synchr
from test_func.test_func_search_kerong_api import search_kerong
from test_func.test_func_downloads_kerong_api import downloads_kerong
from browser_setup import browser

def test_add_kerong(browser):

    # авторизация
    authorization(browser)

    # создание карточки керонг и синхронизация
    auth_kerong(browser)

    # Создание и редактирование карточки, синхронизация
    edit_kerong_synchr(browser)

    # Создание и редактирование карточки
    edit_kerong(browser)

    # Поиск
    search_kerong(browser)

    # Загрузка файла
    downloads_kerong(browser)




