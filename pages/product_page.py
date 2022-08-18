import pytest

from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators


def promo_list():
    PROMO_LIST = ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                  "?promo=offer5", "?promo=offer6", "?promo=offer7", "?promo=offer8", "?promo=offer9"]
    return PROMO_LIST


class ProductPage(MainPage):

    def add_product_to_basket(self):
        add = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add.click()

    def product_added_to_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name.text
        message = self.browser.find_element(*ProductPageLocators.CONFIRMATION_MESSAGE)
        message = message.text
        assert product_name == message, pytest.param(self.browser.current_url.split("/")[-1],
                                                     marks=pytest.mark.xfail(reason="Not critical bug"))

    def product_price_added_to_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price.text.split(" ") [0]
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        price_in_basket = price_in_basket.text.split(" ") [0]
        assert product_price == price_in_basket, "Price in basket is not the same as a product price"

