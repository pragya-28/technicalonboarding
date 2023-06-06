import pytest
import os
import time

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from creds import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY

@pytest.fixture(scope="module", params=[{
    'platformName': 'Android',
    'platformVersion': '11.0',
    'deviceName': 'OnePlus 9',
    'app': 'bs://9efe81dd25c709c3d1561af7f1ad3a086963f370'
},
{
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'OnePlus 8',
    'app': 'bs://9efe81dd25c709c3d1561af7f1ad3a086963f370'
}])

def desired_caps(request):
    return request.param

def common_code(cap):
    try:
        driver = webdriver.Remote("https://"+BROWSERSTACK_USERNAME+":"+BROWSERSTACK_ACCESS_KEY+"@hub-cloud.browserstack.com/wd/hub", cap)
        return driver
    except Exception as e:
        print(e)
    return driver


def test_open_wikipedia(desired_caps):
    try:
        driver = common_code(desired_caps)
        wait = WebDriverWait(driver, 10)
        search_element = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")))
        assert search_element.is_displayed()
        search_element.click()
        driver.quit()
    except:
        driver.quit()

def test_view_results(desired_caps):
    try:
        driver = common_code(desired_caps)
        wait = WebDriverWait(driver, 10)
        search_element = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")))
        search_element.click()
        search_input = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")))
        search_input.send_keys("BrowserStack")
        time.sleep(5)
        search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        assert (len(search_results) > 0)
        driver.quit()
    except:
        driver.quit()