import time
from selenium.webdriver.common.by import By


def test_item_page_has_add_to_basket_button(browser):
    # Ссылка на товар из задания
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    # Открываем страницу
    browser.get(link)

    # ВАЖНО: Критерий проверяющих — пауза 30 секунд для визуальной проверки языка
    time.sleep(30)

    # Ищем кнопку добавления в корзину по уникальному CSS-селектору
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Проверяем наличие кнопки (используем assert)
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена на странице!"