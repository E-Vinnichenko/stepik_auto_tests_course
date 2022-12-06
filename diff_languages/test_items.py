from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_diff_languages(browser):
    browser.get(link)
    time.sleep(20)
    
    # Check unique button
    check_unique = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form button")    
    assert len(check_unique) == 1, "Its not unique"