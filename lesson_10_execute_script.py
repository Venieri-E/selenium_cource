from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text

y = calc(x)
print(y)

try:
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()