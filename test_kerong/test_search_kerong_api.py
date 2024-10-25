# авторизация и поиск керонг апи

from test_kerong.test_authorization import authorization
from test_func.test_func_search_kerong_api import search_kerong
from browser_setup import browser

def test_search_kerong(browser):

    # Авторизация
    authorization(browser)

    # поиск карточки керонг апи
    search_kerong(browser)



