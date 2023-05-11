from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("===Start Test===")
try:
    link = "https://testpages.herokuapp.com/styled/find-by-playground-test.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_1 = browser.find_elements(By.ID, "p1")
    time.sleep(1)
    print("Element 1" + " FOUND")

    element_2 = browser.find_elements(By.CLASS_NAME, "pName26")
    time.sleep(1)
    print("Element 2" + " FOUND")

    element_3 = browser.find_elements(By.ID, "a27")
    time.sleep(1)
    print("Element 3" + " FOUND")


finally:
    time.sleep(5)
    browser.quit()
print("===End of Test===")
