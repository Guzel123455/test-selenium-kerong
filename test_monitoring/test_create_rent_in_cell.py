# Мониторинг. Зона. Выбрать свободную ячейку. Создать аренду

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_create_rent_in_cell import create_rent_in_cell


def test_create_rent_in_cell(browser):

    # Вызов функции авторизации
    authorization(browser)

    # создать аренду
    create_rent_in_cell(browser)