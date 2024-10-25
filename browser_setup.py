from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
import pytest

@pytest.fixture
def browser():
    # Настройка опций для Chrome
    options = Options()
    options.add_argument('--log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--silent')

    service = Service()
    browser = webdriver.Chrome(service=service, options=options)
    browser.get("http://192.168.25.137")
    browser.set_window_size(1920, 1080)
    browser.maximize_window()
    yield browser
    browser.quit()