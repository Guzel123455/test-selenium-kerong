# создание карточки керонг, платы BU, CU, замков, ТИ, идентиф

from test_kerong.test_authorization import authorization
from test_func.test_func_add_kerong_api import add_kerong
from test_func.test_func_add_plata_BU import add_card_BU
from test_func.test_func_add_plata_CU import add_card_CU
from test_func.test_func_add_zone_publ import add_zone_publ
from test_func.test_func_add_lock import add_lock
from test_func.test_func_add_type_identif import add_type_ident
from test_func.test_func_add_identif import add_ident
from test_func.test_func_add_client import add_client
from browser_setup import browser

def test_add_all(browser):
    print()
    # авторизация
    authorization(browser)

    # соединение керонг
    add_kerong(browser)
    print()

    # создание BU
    add_card_BU(browser)
    print()

    # создание CU
    add_card_CU(browser)
    print()

    # создание зоны
    add_zone_publ(browser)
    print()

    # создание замков
    add_lock(browser)
    print()

    # создание типа идентиф
    add_type_ident(browser)
    print()

    # создание идентиф
    add_ident(browser)
    print()

    # добавление клиента
    add_client(browser)
    print()