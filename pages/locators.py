from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM_PRESENT = (By.CSS_SELECTOR, "#login_form")

    SIGNUP_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    SIGNUP_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    SIGNUP_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "#id_registration-password2")
    SIGNUP_FORM_PRESENT = (By.CSS_SELECTOR, "register_form")

    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, ".alertinner.wicon")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in strong")


class BasketPageLocators:
    PRODUCTS_BLOCK = (By.CSS_SELECTOR, "basket_formset")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
