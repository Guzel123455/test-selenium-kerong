# Отчеты. Журнал событий. Таблица. Фильтр на Операция с клиентом

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_reports.test_func_reports.test_func_event_log_filter_CLIENT import event_log_filter_client


def test_event_log_filter_client(browser):

    authorization(browser)
    event_log_filter_client(browser)