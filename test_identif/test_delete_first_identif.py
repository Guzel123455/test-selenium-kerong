#  Идентификаторы. Удаление первого в списке идентификатора

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_identif.test_func_identif.test_func_delete_first_identif import delete_first_identif


def test_delete_first_identif(browser):

    #авторизация
    authorization(browser)

    # удаление
    delete_first_identif(browser)