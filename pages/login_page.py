from pages.main_page import MainPage
from pages.locators import LoginPageLocators
import time

class LoginPage(MainPage):
    def should_be_login_url(self):
        current_url = self.browser.current_url()
        assert "login" in current_url, "This is not Login Page"

    def should_be_login_form(self):
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM_PRESENT)
        assert login_form is True, "Login form is not on the page"

    def should_be_register_form(self):
        register_form = self.is_element_present(*LoginPageLocators.SIGNUP_FORM_PRESENT)
        assert register_form, "Register form is not on the page"

    def register_new_user(self):
        email = self.browser.find_element(*LoginPageLocators.SIGNUP_EMAIL)
        email.send_keys(str(time.time()) + "@fakemail.org")
        password = self.browser.find_element(*LoginPageLocators.SIGNUP_PASSWORD)
        password_value = str(time.time()) + "testpass"
        password.send_keys(password_value)
        password_confirmation = self.browser.find_element(*LoginPageLocators.SIGNUP_PASSWORD_CONFIRMATION)
        password_confirmation.send_keys(password_value)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()
        assert self.is_element_present(*LoginPageLocators.CONFIRMATION_MESSAGE), "Confirmation message isn't on the " \
                                                                                 "page probably user is not registered"
