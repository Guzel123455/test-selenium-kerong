from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
import pytest



@pytest.fixture(scope="session")
def browser():
    # Настройка опций для Chrome
    options = Options()
    options.add_argument('--log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--silent')
    # options.add_argument('--headless') # безголовый режим
    # options.add_argument('--disable-gpu')


    service = Service()
    browser = webdriver.Chrome(service=service, options=options)
    browser.get("http://192.168.25.153:8081")
    browser.set_window_size(1920, 1080)
    browser.maximize_window()
    yield browser
    browser.quit()

