from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_form")

class RegisterPageLocators():
    REGISTER_PAGE = (By.CSS_SELECTOR, "#register_form")

class ADDTOBASKET():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MSG_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner")
    NAME_BOOK_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")