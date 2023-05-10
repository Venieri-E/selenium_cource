from product_page import ProductPage
import pytest
import time
import pytest

# def test_guest_can_add_product_to_basket(browser):
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#    page = ProductPage(browser)
#    page.open()
#    page.add_to_card()
   # page.should_be_success_msg()

@pytest.mark.need_review
def test_guest_can_delete_product_from_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_card()
    page.delete_from_basket()

@pytest.mark.need_review
def test_guest_can_go_to_review_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(browser, link)
    page.open()
    page.write_a_review()

@pytest.mark.need_review
def test_guest_can_go_to_home_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_home_page_from_heading()