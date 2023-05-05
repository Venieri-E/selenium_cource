import time
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(5)

driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
time.sleep(5)

textarea = driver.find_element(By.NAME, "username")
textarea.send_keys("Jeneok")

time.sleep(3)

textarea = driver.find_element(By.NAME, "password")
textarea.send_keys("pasword")

time.sleep(3)

textarea = driver.find_element(By.NAME, "comments")
textarea.clear()
time.sleep(5)
textarea.send_keys("Skills:Python Basic Knowledge ")

time.sleep(3)


submit_button = driver.find_element(By.CSS_SELECTOR, ".styled-click-button")
submit_button.click()
time.sleep(5)

driver.quit()