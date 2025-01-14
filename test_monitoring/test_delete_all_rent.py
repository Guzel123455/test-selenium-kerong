# Мониторинг. Зона. Снять все аренду (будущие и текущие)

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_delete_all_rent import delete_all_rent


def test_delete_all_rent(browser):

    # Вызов функции авторизации
    authorization(browser)

    # удалить аренды
    delete_all_rent(browser)