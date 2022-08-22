from pages.main_page import MainPage
from pages.locators import BasketPageLocators


class BasketPage(MainPage):
    def should_not_be_products_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_BLOCK), "There is an extra " \
                                                                                                "products in empty page"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is no message about" \
                                                                                                        "empty basket"
