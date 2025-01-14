# Зоны. Создание приватной зоны

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_zona.test_func_zona.test_func_add_zone_private import add_zone_private


def test_add_zone_private(browser):

    #авторизация
    authorization(browser)

    #создание зоны
    add_zone_private(browser)