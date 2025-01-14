# Тип идентификатора. Загрузка файла

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_type_identif.test_func_type_identif.test_func_downloads_type_ident import downloads_type_ident



def test_downloads_type_ident(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_type_ident(browser)