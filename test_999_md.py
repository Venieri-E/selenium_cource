import random
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import string

link = "https://999.md/ru/"  # Main page
link2 = "https://simpalsid.com/user/login"  # Log in page
link1 = "https://simpalsid.com/user/register"  # Register page


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser

# Random input values

def generate_random_username(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_email(domain='example.com', length=8):
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    email = f"{username}@{domain}"
    return email


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@allure.epic("Test 999.md site")
class Test_999_md:

    @allure.description("Testing existing elements on Main page")
    def test_main_page_elements(self, browser):
        browser.get(link)
        time.sleep(5)
        with allure.step("Category"):
            browser.find_element(By.ID, "js-categories-toggle").is_displayed()
        with allure.step("Body"):
            browser.find_element(By.CSS_SELECTOR, "body").is_displayed()
        with allure.step("Region"):
            browser.find_element(By.CSS_SELECTOR, "#js-region-toggle > span").is_displayed()
        with allure.step("Register"):
            browser.find_element(By.LINK_TEXT, "регистрация").is_displayed()
        with allure.step("Market"):
            browser.find_element(By.LINK_TEXT, "Market").is_displayed()
        with allure.step("Search field"):
            browser.find_element(By.ID, "js-search-input").is_displayed()
        with allure.step("Search button"):
            browser.find_element(By.CLASS_NAME, "header__search__button").is_displayed()
        with allure.step("Confirm cookies button"):
            browser.find_element(By.CLASS_NAME, "cookies-policy__wrapper__elem__confirm").is_displayed()
        with allure.step("Add new announcement"):
            browser.find_element(By.CSS_SELECTOR, "a[data-autotest='add_ad']").is_displayed()
        with allure.step("Category: 'Готовимся к лету'"):
            browser.find_element(By.CSS_SELECTOR, "a[data-category='6881']").is_displayed()
        with allure.step("Category: 'Транспорт'"):
            browser.find_element(By.CSS_SELECTOR, "a[data-category='658']").is_displayed()
        with allure.step("Category: 'Недвижимость'"):
            browser.find_element(By.CSS_SELECTOR, "a[data-category='270']").is_displayed()
        with allure.step("Log in"):
            browser.find_element(By.LINK_TEXT, "вход").is_displayed()

    @allure.description("Testing existing elements Sign in page")
    def test_sing_in_page_elements(self, browser):
        browser.get(link2)
        with allure.step("Login field"):
            browser.find_element(By.CSS_SELECTOR, "input[name='login']").is_displayed()
        with allure.step("Password field"):
            browser.find_element(By.CSS_SELECTOR, "input[name='password']").is_displayed()
        with allure.step("Enter button"):
            browser.find_element(By.CSS_SELECTOR, "button.login__form__footer__submit[type='submit']").is_displayed()
        with allure.step("Forgot password"):
            browser.find_element(By.CSS_SELECTOR, "a.login__form__footer__forget[type='button'][href^='/user/forgot']")

    @allure.description("Testing existing elements on register page")
    def test_register_page_elements(self, browser):
        browser.get(link1)
        with allure.step("Email field"):
            browser.find_element(By.CSS_SELECTOR, "input[name='email']").is_displayed()
        with allure.step("Name field"):
            browser.find_element(By.CSS_SELECTOR, "input[name='login']").is_displayed()
        with allure.step("Password field"):
            browser.find_element(By.CSS_SELECTOR, "input[name='password']").is_displayed()
        with allure.step("Accept checkbox"):
            browser.find_element(By.CSS_SELECTOR, "input#agree-rules[type='checkbox'][required]").is_displayed()
        with allure.step("Register button"):
            browser.find_element(By.CLASS_NAME, "login__form__footer__submit").is_displayed()
        with allure.step("Register via Google"):
            browser.find_element(By.CLASS_NAME, "is-google").is_displayed()
        with allure.step("Register via Facebook"):
            browser.find_element(By.CLASS_NAME, "is-facebook").is_displayed()
            print("\nEnd of test..")
            time.sleep(1)

    @allure.description("Testing register page")
    def test_register_page(self, browser):
        """Test with random values"""
        browser.get(link1)
        with allure.step("Input Name field"):
            name_field = browser.find_element(By.CSS_SELECTOR, "input[name='login']")
            random_username = generate_random_username()
            name_field.send_keys(random_username)
        with allure.step("Input Email field"):
            email_field = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
            random_email = generate_random_email()
            email_field.send_keys(random_email)
        with allure.step("Input Password field"):
            pass_field = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
            random_pass = generate_random_password()
            pass_field.send_keys(random_pass)
        with allure.step("Accept checkbox"):
            browser.find_element(By.CSS_SELECTOR, "input#agree-rules[type='checkbox'][required]").click()
            time.sleep(3)
        with allure.step("Register button"):
            browser.find_element(By.CLASS_NAME, "login__form__footer__submit").click()

    @allure.description("Testing login in page")
    def test_login_page_with_invalid_credential(self, browser):
        """Input random values"""
        browser.get(link2)
        with allure.step("Input Login field"):
            login_field = browser.find_element(By.CSS_SELECTOR, "input[name='login']")
            random_login = generate_random_username()
            login_field.send_keys(random_login)
        with allure.step("Input Password field"):
            password_field = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
            random_pass = generate_random_password()
            password_field.send_keys(random_pass)
        with allure.step("Click Enter button"):
            browser.find_element(By.CSS_SELECTOR, "button.login__form__footer__submit[type='submit']").click()
            time.sleep(3)
        browser.quit()
