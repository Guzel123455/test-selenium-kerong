# Платы. Редактирование платы BU

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_plata.test_func_plata.test_func_edit_plata_BU import edit_card_BU


def test_edit_card_BU(browser):

    # авторизация
    authorization(browser)

    # редактирование платы
    edit_card_BU(browser)
