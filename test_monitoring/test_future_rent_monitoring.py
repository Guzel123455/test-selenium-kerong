# Мониторинг. Зона. Выбрать свободную ячейку. Создать аренду на следующий день.

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_future_rent_monitoring import future_rent_monitoring


def test_future_rent_monitoring(browser):

    # авторизация
    authorization(browser)

    # арендa на следующий день
    future_rent_monitoring(browser)