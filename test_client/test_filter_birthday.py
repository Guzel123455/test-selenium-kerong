# Клиенты. Фильтр по дате рождения

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_filter_birthday import filter_birthday


def test_filter_birthday(browser):

    # Вызов функции авторизации
    authorization(browser)

    # фильтрация
    filter_birthday(browser)
