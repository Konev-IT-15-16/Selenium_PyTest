import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Добавляем параметр командной строки --language
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es, fr, etc.")


@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение языка из командной строки
    user_language = request.config.getoption("language")

    # Настраиваем опции для Chrome, чтобы установить язык браузера
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    print(f"\nstart browser for test with language {user_language}..")

    # Инициализируем браузер с нужными опциями
    browser = webdriver.Chrome(options=options)

    yield browser

    print("\nquit browser..")
    browser.quit()