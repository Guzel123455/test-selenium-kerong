# Отчеты. Журнал событий. Таблица. Фильтр на Операция с арендой

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_reports.test_func_reports.test_func_event_log_filter_RENT import event_log_filter_rent


def test_event_log_filter_rent(browser):

    authorization(browser)
    event_log_filter_rent(browser)