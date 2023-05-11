from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("=== Start Test===")
try:
    link = "https://testpages.herokuapp.com/styled/iframes-test.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_1 = browser.find_element(By.TAG_NAME, "iFrame")
    time.sleep(2)

    element_2 = browser.find_element(By.CSS_SELECTOR, "[id='iframe59']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element_2)
    time.sleep(2)


finally:
    time.sleep(5)
    browser.quit()
print("===End of Test===")
