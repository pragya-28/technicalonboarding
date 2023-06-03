import time
import os
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from creds import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY, BROWSERSTACK_EMAIL, BROWSERSTACK_PWD


userName = BROWSERSTACK_USERNAME
accessKey = BROWSERSTACK_ACCESS_KEY

versions = [
    {
    "os" : "Windows",
    "osVersion" : "11",
    "browserVersion" : "latest-beta",
    "browserName" : "Chrome",
    "sessionName" : "BStack Build Name:Chrome",
    "userName": userName,
    "accessKey": accessKey
    },
    {
    "os" : "Windows",
    "osVersion" : "11",
    "browserVersion" : "latest",
    "browserName" : "Firefox",
    "sessionName" : "BStack Build Name:Firefox",
    "userName": userName,
    "accessKey": accessKey
    },
    {
    "os" : "OS X",
    "osVersion" : "Ventura",
    "browserVersion" : "16.0",
    "sessionName" : "BStack Build Name:Safari",
    "browserName" : "Safari",
    "userName": userName,
    "accessKey": accessKey
    },
    {
    "os" : "Windows",
    "osVersion" : "10",
    "browserVersion" : "11.0",
    "browserName" : "IE",
    "sessionName" : "BStack Build Name:IE",
    "userName": userName,
    "accessKey": accessKey
    }
]

def get_driver(browser):
    if browser == 'Chrome':
        return webdriver.ChromeOptions()
    if browser == 'Firefox':
        return webdriver.FirefoxOptions()
    if browser == 'Safari':
        return webdriver.ChromeOptions()
    if browser == 'IE':
        return webdriver.IeOptions()

for version in versions:
    print(version['browserName'])
    options = get_driver(version['browserName'])
    options.set_capability('bstack:options', version)
    driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)
    
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.browserstack.com/users/sign_in")

    email_field = wait.until(EC.visibility_of_element_located((By.ID, "user_email_login")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "user_password")))

    email_field.send_keys(BROWSERSTACK_EMAIL)
    password_field.send_keys(BROWSERSTACK_PWD)
    password_field.send_keys(Keys.RETURN)

    wait.until(EC.url_contains("dashboard"))

    browser_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='accordion__header os-section__list os-section__list--windows-icon ']//div[@class='os-section__accordion-header']")))
    browser_icon.click()

    edge_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Windows 11']")))
    edge_icon.click()

    run_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='edge 114 beta']")))
    run_button.click()
    time.sleep(20)
    
    driver.close()
    driver.quit()
    print('test finish')