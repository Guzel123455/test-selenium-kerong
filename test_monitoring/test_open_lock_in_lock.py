# Мониторинг. Зона. Открыть замок внутри ячейки


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_open_lock_in_lock import open_lock_in_lock



def test_open_lock_in_lock(browser):

    # авторизация
    authorization(browser)

    # Открыть ячейку
    open_lock_in_lock(browser)