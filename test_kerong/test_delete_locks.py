# удаление набора замков, первый в списке

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_delete_locks import delete_locks

def test_delete_locks(browser):

    print()
    # авторизация
    authorization(browser)

    # удаление набора замков
    delete_locks(browser)
