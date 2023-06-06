import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.options.ios import XCUITestOptions
from creds import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY

#Android (latest version)#
desired_cap = [{
    "platformName" : "android",
    "platformVersion" : "13.0",
    "deviceName" : "Google Pixel 7 Pro",
    "app" : "bs://9efe81dd25c709c3d1561af7f1ad3a086963f370",
}]

for i in desired_cap:
    print('Android test starts')
    driver = webdriver.Remote("https://"+BROWSERSTACK_USERNAME+":"+BROWSERSTACK_ACCESS_KEY+"@hub-cloud.browserstack.com/wd/hub", i)
    search_element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")))
    search_element.click()
    search_input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")))
    search_input.send_keys("BrowserStack")
    time.sleep(5)
    search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    assert (len(search_results) > 0)
    driver.quit()
    print('Android test finish')

#iPhone (latest version)#
caps = [{
    "platformName" : "ios",
    "platformVersion" : "16.0",
    "deviceName" : "iPhone 14 Pro", # NOT running for 14 Pro Max
    "app" : "bs://a3129b2292fe6e8544f151efa019555ab058ac97",
}]
for i in caps:
    print('iphone test starts')
    options = XCUITestOptions().load_capabilities(i)
    driver = webdriver.Remote("https://"+BROWSERSTACK_USERNAME+":"+BROWSERSTACK_ACCESS_KEY+"@hub-cloud.browserstack.com/wd/hub", options=options)
    text_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Button"))
    )
    text_button.click()
    text_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
    )
    text_input.send_keys("hello@browserstack.com"+"\n")
    time.sleep(5)
    text_output = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Output"))
    )
    if text_output!=None and text_output.text=="hello@browserstack.com":
        assert True
    else:
        assert False
    driver.quit()
    print('iphone test finish')