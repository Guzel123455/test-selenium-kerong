# Идентификаторы. Загрузка файла

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_identif.test_func_identif.test_func_downloads_ident import downloads_ident



def test_downloads_ident(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_ident(browser)