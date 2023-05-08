# checking site http://suninjuly.github.io/get_attribute.html
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x_find = x_element.get_attribute("valuex")
    x = x_find
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_checked = robot_radio.get_attribute("checked")
    print("value of people radio: ", robot_checked)
    assert robot_checked is not None, "Robot radio is not selected by default"

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()