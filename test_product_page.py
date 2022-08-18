import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasePage(browser, link)
    page.open()
    add_product = ProductPage(browser, browser.current_url)
    add_product.add_product_to_basket()
    add_product.solve_quiz_and_get_code()
    add_product.product_added_to_basket_message()
