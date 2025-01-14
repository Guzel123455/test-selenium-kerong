# Отчеты. Журнал событий. Таблица. Фильтр по дате

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_reports.test_func_reports.test_func_event_log_filter_DATE import event_log_filter_date


def test_event_log_filter_date(browser):

    authorization(browser)
    event_log_filter_date(browser)