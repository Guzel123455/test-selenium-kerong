from browser_setup import browser
import pytest
from test_auth.test_authorization import authorization
from test_plata.test_func_plata.test_func_add_plata_BU import add_card_BU
from test_plata.test_func_plata.test_func_add_plata_CU import add_card_CU

class TestPlata:
    def test_run(self, browser):
        authorization(browser)
        add_card_BU(browser)
        add_card_CU(browser)

if __name__ == "__main__":
    pytest.main()