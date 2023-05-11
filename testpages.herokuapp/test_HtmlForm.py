import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Start test")
try:
    link = "https://testpages.herokuapp.com/styled/basic-html-form-test.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    textarea = browser.find_element(By.NAME, "username")
    textarea.send_keys("Jeneok")

    textarea = browser.find_element(By.NAME, "password")
    textarea.send_keys("pasword")

    textarea = browser.find_element(By.NAME, "comments")
    textarea.clear()
    time.sleep(1)
    textarea.send_keys("Skills:Python and Selenium Basic Knowledge ")
    browser.execute_script("return arguments[0].scrollIntoView(true);", textarea)
    time.sleep(1)

    file_btn = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    time.sleep(1)
    file_btn.send_keys('/Users/jeneok/PycharmProjects/pythonProject3/selenium_cource/txt')

    option1 = browser.find_element(By.CSS_SELECTOR, "input[checked='checked']")
    time.sleep(1)
    option1.click()

    check_box_1 = browser.find_element(By.CSS_SELECTOR, "input[value='cb2']")
    check_box_1.click()

    radio_btn = browser.find_element(By.CSS_SELECTOR, "input[value='rd3']")
    radio_btn.click()
    time.sleep(1)

    dropdown_1 = browser.find_element(By.CSS_SELECTOR, "option[value='ms2']")
    dropdown_1.click()

    dropdown_2 = browser.find_element(By.CSS_SELECTOR, "option[value='dd6']")
    dropdown_2.click()
    time.sleep(1)

    submit_button = browser.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
print("End of Test success")
