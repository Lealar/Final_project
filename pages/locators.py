from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_PAGE = (By.CSS_SELECTOR, "#login_form")

class RegisterPageLocators():
    REGISTER_PAGE = (By.CSS_SELECTOR, "#register_form")
