import pytest
from pages.base_page import BasePage
from pages.product_page import ProductPage, promo_list


# @pytest.mark.parametrize('promo', promo_list())
# def test_guest_can_add_product_to_basket(browser, promo):
#     link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/{promo}"
#     page = BasePage(browser, link)
#     page.open()
#
#     add_product = ProductPage(browser, browser.current_url)
#     add_product.add_product_to_basket()
#     add_product.solve_quiz_and_get_code()
#     add_product.product_added_to_basket_message()
#     # add_product.product_price_added_to_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


def test_message_dissapeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_dissapear_success_message()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()
    product_page.go_to_login_page()
