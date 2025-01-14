from browser_setup import browser
from test_auth.test_authorization import authorization
from test_reports.test_func_reports.test_func_event_log_filter_CELL import event_log_filter_cell
from test_reports.test_func_reports.test_func_event_log_filter_CLIENT import event_log_filter_client
from test_reports.test_func_reports.test_func_event_log_filter_IDENTIF import event_log_filter_identif
from test_reports.test_func_reports.test_func_event_log_filter_KR_BU import event_log_filter_kr_bu
from test_reports.test_func_reports.test_func_event_log_filter_KR_CU import event_log_filter_kr_cu
from test_reports.test_func_reports.test_func_event_log_filter_LOCKS import event_log_filter_locks
from test_reports.test_func_reports.test_func_event_log_filter_RENT import event_log_filter_rent
from test_reports.test_func_reports.test_func_event_log_filter_TYPE_IDENTIF import event_log_filter_type_ident
from test_reports.test_func_reports.test_func_event_log_filter_ZONA import event_log_filter_zona


def test_event_log_filter(browser):

    authorization(browser)
    event_log_filter_cell(browser)
    event_log_filter_client(browser)
    event_log_filter_kr_bu(browser)
    event_log_filter_kr_cu(browser)
    event_log_filter_rent(browser)

    event_log_filter_zona(browser)
    event_log_filter_type_ident(browser)
    event_log_filter_identif(browser)
    event_log_filter_locks(browser)
