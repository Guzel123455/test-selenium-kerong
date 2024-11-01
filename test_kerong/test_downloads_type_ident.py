# загрузка файла на странице ТИ


from test_kerong.test_authorization import authorization
from test_func.test_func_downloads_type_ident import downloads_type_ident
from browser_setup import browser


def test_downloads_type_ident(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_type_ident(browser)