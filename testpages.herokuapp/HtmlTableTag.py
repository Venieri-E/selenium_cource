from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("===Start Test===")
try:
    link = "https://testpages.herokuapp.com/styled/tag/table.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_1 = browser.find_elements(By.ID, "mytable")
    time.sleep(1)
    print("Element 'Table'" + " FOUND")

    element_2 = browser.find_elements(By.TAG_NAME, "Name")
    print("Element 'Name'" + " FOUND")

    element_3 = browser.find_elements(By.TAG_NAME, "Amount")
    print("Element 'Amount'" + " FOUND")

    element_4 = browser.find_elements(By.TAG_NAME, "Douglas")
    print("Name 'Douglas'" + " FOUND")

finally:
    time.sleep(2)
    browser.quit()
print("===End of Test===")
