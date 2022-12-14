import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer2"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer2"
        add_product = ProductPage(browser, link)
        add_product.open()
        add_product.add_product_to_basket()
        add_product.solve_quiz_and_get_code()
        add_product.product_added_to_basket_message()
        add_product.product_price_added_to_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer2"
    add_product = ProductPage(browser, link)
    add_product.open()
    add_product.add_product_to_basket()
    add_product.solve_quiz_and_get_code()
    add_product.product_added_to_basket_message()
    add_product.product_price_added_to_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()
    product_page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/growing-object-oriented-software-guided-by-tests_123/"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket()
    page.should_not_be_products_in_empty_basket()
    page.should_be_message_about_empty_basket()

    # def test_user_cant_see_success_message(self, browser):
    #     link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer0"
    #     product_page = ProductPage(browser, link)
    #     product_page.open()
    #     product_page.should_not_be_success_message()

    # def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
    #     link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer0"
    #     product_page = ProductPage(browser, link)
    #     product_page.open()
    #     product_page.add_product_to_basket()
    #     product_page.solve_quiz_and_get_code()
    #     product_page.should_not_be_success_message()
    #
    # def test_message_dissapeared_after_adding_product_to_basket(self, browser):
    #     link = f"http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer0"
    #     product_page = ProductPage(browser, link)
    #     product_page.open()
    #     product_page.add_product_to_basket()
    #     product_page.solve_quiz_and_get_code()
    #     product_page.should_dissapear_success_message()
    #

