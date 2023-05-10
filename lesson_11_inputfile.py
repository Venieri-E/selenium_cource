from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
    firstname.send_keys("Jeneok")

    firstname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
    firstname.send_keys("Venieri")

    email = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
    email.send_keys("email@gmail.com")

    file_btn = browser.find_element(By.ID, "file")
    file_btn.send_keys('/Users/jeneok/PycharmProjects/selenium_cource/txt')

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
