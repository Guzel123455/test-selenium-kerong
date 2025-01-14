# Мониторинг. Зона. Создать аренду

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_create_rent_in_zona import create_rent_in_zona


def test_create_rent_in_zona(browser):

    # Вызов функции авторизации
    authorization(browser)

    # создать аренду
    create_rent_in_zona(browser)