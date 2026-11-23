import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        # Если захотите добавить Firefox, раскомментируйте
        # from selenium.webdriver.firefox.options import Options as FirefoxOptions
        # options = FirefoxOptions()
        # options.set_preference("intl.accept_languages", user_language)
        # browser = webdriver.Firefox(options=options)
        pass
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()