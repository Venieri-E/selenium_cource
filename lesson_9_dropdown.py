from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    x = num1.text

    num2 = browser.find_element(By.ID, "num2")
    y = num2.text

    summ = int(x) + int(y)
    print(str(summ))

    select = Select(browser.find_element(By.ID,  "dropdown"))
    select.select_by_value(str(summ))

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

