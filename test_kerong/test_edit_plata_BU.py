# редактирование карточки BU и проверка наличия карточки

from test_kerong.test_authorization import authorization
from test_func.test_func_edit_plata_BU import edit_card_BU
from browser_setup import browser

def test_edit_card_BU(browser):

    # авторизация
    authorization(browser)

    # редактирование платы
    edit_card_BU(browser)
