# Отчеты. Журнал событий. Таблица. Фильтр на Операции с KR-CU

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_reports.test_func_reports.test_func_event_log_filter_KR_CU import event_log_filter_kr_cu


def test_event_log_filter_kr_cu(browser):

    authorization(browser)
    event_log_filter_kr_cu(browser)