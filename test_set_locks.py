# Добавить замки и ячейки (приватная зона)
# Добавить замки и ячейки (корп зона)
# Добавить замки и ячейки (публичная зона)
# Поиск
# Печать данных
# Удаление набора


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_locks.test_func_locks.test_func_add_lock_priv import add_lock_priv
from test_locks.test_func_locks.test_func_add_lock_corp import add_lock_corp
from test_locks.test_func_locks.test_func_add_lock_publ import add_lock_publ
from test_locks.test_func_locks.test_func_search_locks import search_locks
from test_locks.test_func_locks.test_func_delete_locks import delete_locks
from termcolor import cprint



def test_zona_locks_corp(browser):

    cprint("Авторизация", "green")
    authorization(browser)
    print()

    cprint("Добавить замки и ячейки (приватная зона)", "green")
    add_lock_priv(browser)
    print()

    cprint("Добавить замки и ячейки (корп зона)", "green")
    add_lock_corp(browser)
    print()

    cprint("Добавить замки и ячейки (публичная зона)", "green")
    add_lock_publ(browser)
    print()

    cprint("Поиск", "green")
    search_locks(browser)
    print()

    # Печать данных

    cprint("Удаление набора", "green")
    delete_locks(browser)




