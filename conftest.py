import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language", action='store', default="ru", help="Chose language")

@pytest.fixture(scope="function")
def browser(request):
    langu = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': langu})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\n close browser")
    browser.close()
