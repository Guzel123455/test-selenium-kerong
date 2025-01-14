# Отчеты. Журнал событий. Таблица. Печать данных

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_reports.test_func_reports.test_func_event_log_DOWNLOAD import event_log_download


def test_event_log_download(browser):

    authorization(browser)
    event_log_download(browser)