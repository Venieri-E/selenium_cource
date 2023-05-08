import time
from selenium import webdriver
# """Testing site  - http://suninjuly.github.io/find_link_text"""

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(3)

    link_1 = browser.find_element(By.PARTIAL_LINK_TEXT, "224592")
    link_1.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("JeneOK")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Venieri")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Chisinau")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Moldova")
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
