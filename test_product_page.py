from .pages.product_page import ProductPage
import sys
import pytest
import time

@pytest.mark.parametrize('promo', ["newYear","offer0", "offer1","offer2","offer3","offer4",
                                   "offer5","offer6", pytest.param("offer7" ,marks=pytest.mark.xfail(reason="DIFFRENT NaME BOOKS")),
                                   "offer8","offer9"])

def test_guest_can_add_product_to_basket(browser, promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"
    page = ProductPage(browser, link)
    page.open()
    page.push_button_add_to_basket()
    page.check_book_in_basket()
    page.price_basket_and_book()
    time.sleep(2)

