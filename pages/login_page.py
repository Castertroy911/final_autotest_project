from pages.main_page import MainPage
from pages.locators import LoginPageLocators

class LoginPage(MainPage):
    def should_be_login_url(self):
        current_url = self.browser.current_url()
        assert "login" in current_url, "This is not Login Page"

    def should_be_login_form(self):
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM_PRESENT)
        assert login_form, "Login form is not on the page"

    def should_be_register_form(self):
        register_form = self.is_element_present(*LoginPageLocators.SIGNUP_FORM_PRESENT)
        assert register_form, "Register for is not on the page"