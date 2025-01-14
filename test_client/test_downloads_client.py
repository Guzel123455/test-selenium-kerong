# Клиенты. Загрузка файла

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_downloads_client import downloads_client



def test_downloads_client(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_client(browser)