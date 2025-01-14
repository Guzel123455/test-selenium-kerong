# Авторизация
# Создание карточки kerong, синхронизация
# Создание карточки BU
# Создание карточки СU
# Создание зоны (приватная)
# Создание набора замков (для приватной зоны)
# Создание зоны (корпоративная)
# Создание набора замков (для корп зоны)
# Создание зоны (публичная)
# Создание набора замков (для публ зоны)
# Создание Типа идентфикатора
# Создание идентификатора
# Добавление клиента

import pytest
from browser_setup import browser
from test_auth.test_authorization import authorization
from test_kerong_api.test_func_kerong_api.test_func_add_kerong_api import add_kerong
from test_plata.test_func_plata.test_func_add_plata_BU import add_card_BU
from test_plata.test_func_plata.test_func_add_plata_CU import add_card_CU
from test_zona.test_func_zona.test_func_add_zone_private import add_zone_private
from test_locks.test_func_locks.test_func_add_lock_priv import add_lock_priv
from test_zona.test_func_zona.test_func_add_zone_corp import add_zone_corp
from test_locks.test_func_locks.test_func_add_lock_corp import add_lock_corp
from test_zona.test_func_zona.test_func_add_zone_publ import add_zone_publ
from test_locks.test_func_locks.test_func_add_lock_publ import add_lock_publ
from test_type_identif.test_func_type_identif.test_func_add_type_identif import add_type_ident
from test_identif.test_func_identif.test_func_add_identif import add_ident
from test_client.test_func_client.test_func_add_client import add_client
from termcolor import cprint

class TestPlata:
    def test_run(self, browser):

        cprint("Авторизация", "green")
        authorization(browser)

        cprint("Создание карточки kerong, синхронизация", "green")
        add_kerong(browser)
        print()

        cprint("Создание карточки BU", "green")
        add_card_BU(browser)
        print()

        cprint("Создание карточки СU", "green")
        add_card_CU(browser)
        print()

        cprint("Создание зоны (приватная)", "green")
        add_zone_private(browser)
        print()

        cprint("Создание набора замков (для приватной зоны)", "green")
        add_lock_priv(browser)
        print()

        cprint("Создание зоны (корпоративная)", "green")
        add_zone_corp(browser)
        print()

        cprint("Создание набора замков (для корп зоны)", "green")
        add_lock_corp(browser)
        print()

        cprint("Создание зоны (публичная)", "green")
        add_zone_publ(browser)
        print()

        cprint("Создание набора замков (для публ зоны)", "green")
        add_lock_publ(browser)
        print()

        cprint("Создание Типа идентфикатора", "green")
        add_type_ident(browser)
        print()

        cprint("Создание идентификатора", "green")
        add_ident(browser)
        print()

        cprint("Добавление клиента", "green")
        add_client(browser)
        print()

if __name__ == "__main__":
    pytest.main()