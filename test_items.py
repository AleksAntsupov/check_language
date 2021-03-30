import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_can_see_button(browser):
    browser.get(link)
    
    time.sleep(30)
    
    buttod_ad = browser.find_element_by_xpath("//button[contains(@class, 'btn-add-to-basket')]")
    
    assert buttod_ad is not None