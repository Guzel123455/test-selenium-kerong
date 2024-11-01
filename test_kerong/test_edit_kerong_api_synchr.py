# редактирование керонг апи , синхронизировать

from test_kerong.test_authorization import authorization
from test_func.test_func_edit_kerong_api_synchr import edit_kerong_synchr
from browser_setup import browser

def test_edit_kerong_synchr(browser):

    # авторизация
    authorization(browser)

    # редактироние, синхронизация
    edit_kerong_synchr(browser)



