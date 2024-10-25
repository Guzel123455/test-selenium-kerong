# Создание карточки Зоны и проверка наличия карточки

from test_func.test_func_add_zone_publ import create_and_zone
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_add_plata_CU(browser):

    #авторизация
    authorization(browser)

    #создание зоны
    create_and_zone(browser)