from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM_PRESENT = (By.CSS_SELECTOR, "#login_form")

    SIGNUP_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    SIGNUP_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    SIGNUP_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "#id_registration-password2")
    SIGNUP_FORM_PRESENT = (By.CSS_SELECTOR, "register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, ".alert-success > .alertinner")