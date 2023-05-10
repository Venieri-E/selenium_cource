from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    new_window_name = browser.window_handles[1]
    browser.switch_to.window(new_window_name)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(str(y))

    browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(5)
    browser.quit()