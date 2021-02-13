from .base_page import BasePage
from .locators import ADDTOBASKET

class ProductPage(BasePage):
    def push_button_add_to_basket(self):
        self.browser.find_element(*ADDTOBASKET.BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def check_book_in_basket(self):
        assert self.is_element_present(*ADDTOBASKET.MSG_BOOK_IN_BASKET), "Product is not present"
        assert self.is_element_present(*ADDTOBASKET.NAME_BOOK_ON_PAGE), "Message about adding is not presented"
        first_message = self.browser.find_element(*ADDTOBASKET.MSG_BOOK_IN_BASKET).text
        name_book = self.browser.find_element(*ADDTOBASKET.NAME_BOOK_ON_PAGE).text
        assert name_book in first_message, f"Название книг не совпадает {name_book}, {first_message}"

    def price_basket_and_book(self):
        assert self.is_element_present(*ADDTOBASKET.PRICE_BASKET), "Message basket total is not presented"
        assert self.is_element_present(*ADDTOBASKET.PRICE_BOOK), "Product price is not presented"
        price_basket = self.browser.find_element(*ADDTOBASKET.PRICE_BASKET).text.split(" ")
        print(f"Стоимость корзины: {price_basket[0]}")
        price_book = self.browser.find_element(*ADDTOBASKET.PRICE_BOOK).text.split(" ")
        assert price_book[0] == price_basket[0], f"Цены разные, цена книги: {price_book}, цена корзины: {price_basket}"

