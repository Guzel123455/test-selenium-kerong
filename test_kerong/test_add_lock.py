# Создание набора замков и проверка наличия

from test_func.test_func_add_lock import create_and_lock
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_add_plata_CU(browser):

    #авторизация
    authorization(browser)

    #создание зоны
    create_and_lock(browser)