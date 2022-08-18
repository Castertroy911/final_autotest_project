from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators


class ProductPage(MainPage):
    def add_product_to_basket(self):
        add = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add.click()

    def product_added_to_basket_message(self):
        message = self.is_element_present(*ProductPageLocators.CONFIRMATION_MESSAGE)
        assert message is True, "Product was not added to the basket"