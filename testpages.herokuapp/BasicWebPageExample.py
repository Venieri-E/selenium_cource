from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://testpages.herokuapp.com/styled/basic-web-page-test.html")
    element_1 = browser.find_elements(By.CLASS_NAME, "main")
    time.sleep(2)

    element_2 = browser.find_elements(By.CLASS_NAME, "sub")


finally:
    time.sleep(5)
    browser.quit()
