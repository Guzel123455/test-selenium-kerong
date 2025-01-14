# Зоны. Загрузка файла

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_zona.test_func_zona.test_func_downloads_zona import downloads_zona



def test_downloads_zona(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_zona(browser)