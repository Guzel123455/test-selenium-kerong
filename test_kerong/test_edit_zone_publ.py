# добавление публичной зоны и редактирование

from test_func.test_func_edit_zone_publ import edit_zone_publ
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_edit_zone_publ(browser):

    #авторизация
    authorization(browser)

    #создание и редактирование зоны
    edit_zone_publ(browser)