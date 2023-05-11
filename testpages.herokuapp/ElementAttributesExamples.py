from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("===Start Test===")
try:
    link = "https://testpages.herokuapp.com/styled/attributes-test.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_1 = browser.find_elements(By.CLASS_NAME, "class-attribute")
    time.sleep(2)
    print("Element 1" + " FOUND")

    button_add_attribute = browser.find_element(By.ID, "jsattributes")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_add_attribute)
    button_add_attribute.click()
    print("Button" + " 'Add Another Attribute'" + " FOUND")
    get_nextid = browser.find_element(By.ID, "jsattributes").get_attribute("nextid")
    print("Next ID = " + get_nextid)


finally:
    time.sleep(5)
    browser.quit()
print("===End of Test===")
