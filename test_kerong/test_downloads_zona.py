# загрузка файла на странице Зоны

from test_kerong.test_authorization import authorization
from test_func.test_func_downloads_zona import downloads_zona
from browser_setup import browser


def test_downloads_zona(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_zona(browser)