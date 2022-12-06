import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser: es or fr")
                     

@pytest.fixture(scope="function")
def browser(request):
    # Считываем указанный язык
    user_language = request.config.getoption("language")
    
    # Передаем язык в методе add_experimental_option
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    # Открываем браузер с нужными опциями
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
    