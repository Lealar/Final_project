from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, f"Wrong URL: {self.url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_PAGE), "Login element is not exist"

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_PAGE), "Registration element is not exist"