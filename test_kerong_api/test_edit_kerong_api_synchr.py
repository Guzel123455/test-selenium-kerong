# Kerong Api. Редактирование соединения с синхронизацией

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_kerong_api.test_func_kerong_api.test_func_edit_kerong_api_synchr import edit_kerong_synchr


def test_edit_kerong_synchr(browser):

    # авторизация
    authorization(browser)

    # редактироние, синхронизация
    edit_kerong_synchr(browser)



