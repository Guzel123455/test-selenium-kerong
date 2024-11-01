# загрузка файла на странице идентификаторы


from test_kerong.test_authorization import authorization
from test_func.test_func_downloads_ident import downloads_ident
from browser_setup import browser


def test_downloads_ident(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_ident(browser)