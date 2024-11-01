# добавление и проверка наличия карточки

from test_func.test_func_add_plata_BU import add_card_BU
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_add_card_BU(browser):

    # авторизация
    authorization(browser)

    # создание платы BU
    add_card_BU(browser)