# Мониторинг. Зона. Снять статус авария

from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_remove_accident_status import remove_accident_status

def test_remove_accident_status(browser):

    # авторизация
    authorization(browser)

    # Снять статус авария
    remove_accident_status(browser)