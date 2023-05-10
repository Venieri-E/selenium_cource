from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn .btn-default")

class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_CARD_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MSG_TITLE = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    SUCCESS_MSG_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    DELETE_FROM_BASKET = (By.CSS_SELECTOR, ".inline [href]")
    VIEW_BASKET = (By.CLASS_NAME, "btn-default")
    WRITE_REVIEW_BUTTON = (By.ID, "write_review")
    HOME_PAGE = (By.XPATH, "//li/a[text()='Home']")
    HEADING = (By.XPATH, "//div/a[text()]='Oscar'")


class MainPageLocators:
    pass