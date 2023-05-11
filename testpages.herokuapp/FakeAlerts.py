from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("=== Start Test===")
try:
    link = "https://testpages.herokuapp.com/styled/alerts/fake-alert-test.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element(By.ID, "fakealert").click()
    time.sleep(2)
    accept_1 = browser.find_element(By.ID, "dialog-ok").click()

    button_2 = browser.find_element(By.ID, "modaldialog").click()
    time.sleep(2)
    accept_2 = browser.find_element(By.CLASS_NAME, "dialog-button").click()


finally:
    time.sleep(5)
    browser.quit()
print("===End of Test===")
