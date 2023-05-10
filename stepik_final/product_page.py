from base_page import BasePage
from locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_card(self):
        add_to_card_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BTN)
        add_to_card_btn.click()
    #    self.solve_quiz_and_get_code()

    #def should_be_success_msg(self):
    #   self.should_be_correct_price()

    #def should_be_correct_title(self):
    #    assert self.get_element_text(*ProductPageLocators.TITLE) == \
    #           self.get_element_text(*ProductPageLocators.SUCCESS_MSG_TITLE), "title in success msg is not correct"

    #def should_be_correct_price(self):
    #    assert self.get_element_text(*ProductPageLocators.PRICE) == \
    #           self.get_element_text(*ProductPageLocators.SUCCESS_MSG_PRICE), "price in success msg is not correct"


    def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    def delete_from_basket(self):
        add_to_card_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BTN)
        add_to_card_btn.click()
        go_to_basket = self.browser.find_element(*ProductPageLocators.VIEW_BASKET)
        go_to_basket.click()
        delete_good_from_basket = self.browser.find_element(*ProductPageLocators.DELETE_FROM_BASKET)
        delete_good_from_basket.click()

    def write_a_review(self):
        write_review_button = self.browser.find_element(*ProductPageLocators.WRITE_REVIEW_BUTTON)
        write_review_button.click()

    def go_to_home_page(self):
        open_home_page = self.browser.find_element(*ProductPageLocators.HOME_PAGE)
        open_home_page.click()

    def go_to_home_page_from_heading(self):
        go_to_main_page = self.browser.find.element(*ProductPageLocators.HEADING)
        go_to_main_page.click()