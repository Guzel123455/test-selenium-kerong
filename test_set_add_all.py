# создание карточки керонг, платы BU, CU, замков, ТИ, идентиф

from test_kerong.test_authorization import authorization
from test_func.test_func_add_kerong_api import auth_kerong
from test_func.test_func_add_plata_BU import create_and_check_card_BU
from test_func.test_func_add_plata_CU import create_and_check_card_CU
from test_func.test_func_add_zone_publ import create_and_zone
from test_func.test_func_add_lock import create_and_lock
from test_func.test_func_add_type_identif import create_type_ident
from test_func.test_add_func_identif import create_ident
from browser_setup import browser

def test_add_all(browser):
    # авторизация
    authorization(browser)

    # соединение керонг
    auth_kerong(browser)

    # создание BU
    create_and_check_card_BU(browser)

    # создание CU
    create_and_check_card_CU(browser)

    # создание зоны
    create_and_zone(browser)

    # создание замков
    create_and_lock(browser)

    # создание типа идентиф
    create_type_ident(browser)

    # создание идентиф
    create_ident(browser)