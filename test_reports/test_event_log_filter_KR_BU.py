# Отчеты. Журнал событий. Таблица. Фильтр на Операции с KR-BU

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_reports.test_func_reports.test_func_event_log_filter_KR_BU import event_log_filter_kr_bu


def test_event_log_filter_kr_bu(browser):

    authorization(browser)
    event_log_filter_kr_bu(browser)