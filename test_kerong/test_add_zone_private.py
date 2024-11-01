# добавление приватной зоны и проверка наличия

from test_func.test_func_add_zone_private import add_zone_private
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_add_zone_private(browser):

    #авторизация
    authorization(browser)

    #создание зоны
    add_zone_private(browser)