from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome, firefox")
    parser.addoption('--language', action='store', default='en-gb',
                     help='Choose language: es, fr, en-gb, ru, de, it')

@pytest.fixture(scope="session")
def browser(request):
    lang = request.config.getoption("browser_name")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    print('\nstart Chrome browser...')
    browser = webdriver.Chrome(options=options)
    print('\nstart chrome browser for test..', 'language =', lang)
    yield browser
    print("\nquit browser..")
    browser.quit()