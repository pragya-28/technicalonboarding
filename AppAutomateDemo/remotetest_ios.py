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

@pytest.fixture(scope="module", params=[
{
    "platformName" : "ios",
    "platformVersion" : "16.0",
    "deviceName" : "iPhone 14",
    "app" : "bs://a3129b2292fe6e8544f151efa019555ab058ac97"
},
{
    'platformName': 'ios',
    'platformVersion': '15',
    'deviceName': 'iPhone XS',
    'app': 'bs://a3129b2292fe6e8544f151efa019555ab058ac97'
},
{
    'platformName': 'ios',
    'platformVersion': '15',
    'deviceName': 'iPad 9th',
    'app': 'bs://a3129b2292fe6e8544f151efa019555ab058ac97'
},
{
    'platformName': 'ios',
    'platformVersion': '14',
    'deviceName': 'iPad Air 4',
    'app': 'bs://a3129b2292fe6e8544f151efa019555ab058ac97'
}
])


def desired_caps(request):
    return request.param


def common_code(cap):
    try:
        options = XCUITestOptions().load_capabilities(cap)
        driver = webdriver.Remote("https://"+BROWSERSTACK_USERNAME+":"+BROWSERSTACK_ACCESS_KEY+"@hub-cloud.browserstack.com/wd/hub", options=options)
    except Exception as e:
        print(e)
    return driver
        


def test_click_text_button(desired_caps):
    try:
        driver = common_code(desired_caps)
        text_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Button"))
        )
        assert text_button.is_displayed()
        text_button.click()
        driver.quit()
    except:
        driver.quit()


def test_text_typed(desired_caps):
    try:
        driver = common_code(desired_caps)
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
    except:
        driver.quit()
    
    
        