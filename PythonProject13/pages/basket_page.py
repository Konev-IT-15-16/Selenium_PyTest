from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "В корзине есть товары, хотя она должна быть пуста"

        empty_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "empty" in empty_text.lower() or "пуста" in empty_text.lower(), \
            f"Нет сообщения о том, что корзина пуста. Текст на странице: {empty_text}"