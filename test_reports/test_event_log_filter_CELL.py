# Отчеты. Журнал событий. Таблица. Фильтр на Операция с ячейкой

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_reports.test_func_reports.test_func_event_log_filter_CELL import event_log_filter_cell


def test_event_log_filter_cell(browser):

    authorization(browser)
    event_log_filter_cell(browser)