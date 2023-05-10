from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_cart_button_should_be_present_on_product_page(browser):
    browser.get(url)
    time.sleep(3)
    try:
        cartbutton = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-add-to-basket"))
                    )
    except Exception as ex:
        assert False, "'Add to cart' button is broken"
    assert True