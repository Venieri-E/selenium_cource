from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://testpages.herokuapp.com/styled/alerts/alert-test.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element(By.ID, "alertexamples").click()
    time.sleep(1)
    confirm = browser.switch_to.alert.accept()

    button_2 = browser.find_element(By.ID, "confirmexample").click()
    time.sleep(1)
    confirm_2 = browser.switch_to.alert.accept()

    button_3 = browser.find_element(By.ID, "promptexample").click()
    time.sleep(1)
    confirm_3 = browser.switch_to.alert.accept()


finally:
    time.sleep(2)
    browser.quit()