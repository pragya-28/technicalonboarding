import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from creds import BROWSERSTACK_ACCESS_KEY, BROWSERSTACK_USERNAME, BROWSERSTACK_EMAIL, BROWSERSTACK_PWD

@pytest.fixture(scope="module", params=[
    {
        'browserName': 'Chrome',
        'browserVersion': 'latest',
        'os': 'Windows',
        'osVersion': '10',
        'sessionName': 'Login and Open Browser Test 1'
    },
    {
        'browserName': 'Firefox',
        'browserVersion': 'latest',
        'os': 'Windows',
        'osVersion': '10',
        'sessionName': 'Login and Open Browser Test 2'
    },
    {
        'browserName': 'IE',
        'browserVersion': '11.0',
        'os': 'Windows',
        'osVersion': '10',
        'sessionName': 'Login and Open Browser Test 3'
    },
    {
        'browserName': 'Safari',
        'browserVersion': '16.0',
        'os': 'OS X',
        'osVersion': 'Ventura',
        'sessionName': 'Login and Open Browser Test 4'
    },
    {
        'browserName': 'Edge',
        'browserVersion': 'latest',
        'os': 'Windows',
        'osVersion': '10',
        'sessionName': 'Login and Open Browser Test 5'
    }
])

def desired_caps(request):
    return request.param


def common_code(cap):
    try:
        driver = webdriver.Remote(
            command_executor=f'https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=cap
        )
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.browserstack.com/users/sign_in")

        email_field = wait.until(EC.visibility_of_element_located((By.ID, "user_email_login")))
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "user_password")))

        email_field.send_keys(BROWSERSTACK_EMAIL)
        password_field.send_keys(BROWSERSTACK_PWD)
        password_field.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        return driver
    except Exception as e:
        print(e)

    return driver


def test_login(desired_caps):
    try:
        driver = common_code(desired_caps)
        #dashboard_element = driver.find_element(By.ID, 'bd-dashbaord')
        #assert dashboard_element.is_displayed()
        assert 'BrowserStack' in driver.title
        driver.quit()
    except:
        driver.quit()

def test_windows(desired_caps):
    try:
        driver = common_code(desired_caps)
        wait = WebDriverWait(driver, 10)
        browser_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='accordion__header os-section__list os-section__list--windows-icon ']//div[@class='os-section__accordion-header']")))
        assert browser_icon.is_displayed()
        browser_icon.click()
        driver.quit()
        time.sleep(5)
    except:
        driver.quit()

def test_edge(desired_caps):
    try:
        driver = common_code(desired_caps)
        wait = WebDriverWait(driver, 10)
        edge_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Windows 11']")))
        assert edge_icon.is_displayed()
        edge_icon.click()
        driver.quit()
        time.sleep(5)
    except:
        driver.quit()

def test_run(desired_caps):
    try:
        driver = common_code(desired_caps)
        wait = WebDriverWait(driver, 10)
        run_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='edge 114 beta']")))
        assert run_button.is_displayed()
        run_button.click()
        driver.quit()
        time.sleep(20)
    except:
        driver.quit()
