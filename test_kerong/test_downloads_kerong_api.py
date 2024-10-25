# загрузка файла

from test_kerong.test_authorization import authorization
from test_func.test_func_downloads_kerong_api import downloads_kerong
from browser_setup import browser


def test_add_plata_BU_CU(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_kerong(browser)