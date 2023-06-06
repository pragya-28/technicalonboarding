import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'Android Device',
    'appPackage': 'org.wikipedia',
    'appActivity': '.main.MainActivity',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
wait = WebDriverWait(driver, 10)
search_element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")))
search_element.click()
# language_option = driver.find_elements(MobileBy.XPATH, '//android.widget.Button[contains(@text, "Skip")]')
# if language_option:
#     language_option[0].click()
search_box = wait.until(EC.visibility_of_element_located((MobileBy.ID, 'org.wikipedia:id/search_container')))
search_box.click()
search_input = wait.until(EC.visibility_of_element_located((MobileBy.ID, 'org.wikipedia:id/search_src_text')))
search_input.send_keys("Browserstack")
search_input.click()
search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
assert (len(search_results) > 0)
driver.quit()