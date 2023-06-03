import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from creds import BROWSERSTACK_EMAIL,BROWSERSTACK_PWD


@pytest.fixture(scope="class")
def browserstack_driver_chrome(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def browserstack_driver_firefox(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def browserstack_driver_safari(request):
    driver = webdriver.Safari()
    request.cls.driver = driver
    yield driver
    driver.quit()

class HelperFunctions:
    
    def login_helper(driver):
        time.sleep(5)
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.browserstack.com/users/sign_in")

        email_field = wait.until(EC.visibility_of_element_located((By.ID, "user_email_login")))
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "user_password")))

        email_field.send_keys(BROWSERSTACK_EMAIL)
        password_field.send_keys(BROWSERSTACK_PWD)
        password_field.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        
        dashboard_element = driver.find_element(By.ID, 'bd-dashboard')
        assert dashboard_element.is_displayed()

    def dashboard_helper(driver):
        wait = WebDriverWait(driver, 10)
        browser_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='accordion__header os-section__list os-section__list--windows-icon ']//div[@class='os-section__accordion-header']")))
        assert browser_icon.is_displayed()
        browser_icon.click()
        time.sleep(5)

    def edge_icon_helper(driver):
        wait = WebDriverWait(driver, 10)
        edge_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Windows 11']")))
        assert edge_icon.is_displayed()
        edge_icon.click()
        time.sleep(5)

    def launch_helper(driver):
        wait = WebDriverWait(driver, 10)
        run_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='edge 114 beta']")))
        assert run_button.is_displayed()
        run_button.click()
        time.sleep(20)


class TestBrowserStackChrome:
    def test_login(self, browserstack_driver_chrome):
        HelperFunctions.login_helper(browserstack_driver_chrome)

    def test_dashboard(self, browserstack_driver_chrome):
        HelperFunctions.dashboard_helper(browserstack_driver_chrome)

    def test_edge_icon(self, browserstack_driver_chrome):
        HelperFunctions.edge_icon_helper(browserstack_driver_chrome) 

    def test_launch(self, browserstack_driver_chrome):
        HelperFunctions.launch_helper(browserstack_driver_chrome)


class TestBrowserStackFirefox:
    def test_login(self, browserstack_driver_firefox):
        HelperFunctions.login_helper(browserstack_driver_firefox)

    def test_dashboard(self, browserstack_driver_firefox):
        HelperFunctions.dashboard_helper(browserstack_driver_firefox)

    def test_edge_icon(self, browserstack_driver_firefox):
        HelperFunctions.edge_icon_helper(browserstack_driver_firefox) 

    def test_launch(self, browserstack_driver_firefox):
        HelperFunctions.launch_helper(browserstack_driver_firefox) 


class TestBrowserStackSafari:
    def test_login(self, browserstack_driver_safari):
        HelperFunctions.login_helper(browserstack_driver_safari)

    def test_dashboard(self, browserstack_driver_safari):
        HelperFunctions.dashboard_helper(browserstack_driver_safari)

    def test_edge_icon(self, browserstack_driver_safari):
        HelperFunctions.edge_icon_helper(browserstack_driver_safari) 

    def test_launch(self, browserstack_driver_safari):
        HelperFunctions.launch_helper(browserstack_driver_safari)