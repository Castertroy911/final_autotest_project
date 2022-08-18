import time

import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_page import ProductPage, promo_list
from pages.locators import ProductPageLocators


@pytest.mark.parametrize('promo', promo_list())
def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/{promo}"
    page = BasePage(browser, link)
    page.open()
    add_product = ProductPage(browser, browser.current_url)
    add_product.add_product_to_basket()
    add_product.solve_quiz_and_get_code()
    add_product.product_added_to_basket_message()
    # add_product.product_price_added_to_basket()
