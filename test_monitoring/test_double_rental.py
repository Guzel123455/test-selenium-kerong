# Мониторинг. Зона. Добавить аренду к существ.аренде

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_double_rental import double_rental


def test_double_rental(browser):

    # Вызов функции авторизации
    authorization(browser)

    double_rental(browser)