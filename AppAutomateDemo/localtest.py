import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_caps = {
    'platformName': 'Android',
    'platformVersion': '10.0',
    'deviceName': 'Android Device',
    'appPackage': 'org.wikipedia',
    'appActivity': '.main.MainActivity',
}

@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestBrowserStackWikipedia:
    def test_open_wikipedia(self, driver):
        wait = WebDriverWait(driver, 10)
        search_element = wait.until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia")))
        assert search_element.is_displayed()
        search_element.click()

    def test_click_search_box(self, driver):
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.visibility_of_element_located((MobileBy.ID, 'org.wikipedia:id/search_container')))
        assert search_box.is_displayed()
        search_box.click()

    def test_search_browserstack(self, driver):
        wait = WebDriverWait(driver, 10)
        search_input = wait.until(EC.visibility_of_element_located((MobileBy.ID, 'org.wikipedia:id/search_src_text')))
        search_input.send_keys("Browserstack")
        assert search_input.is_displayed()
        search_input.click()

    def test_searched(self, driver):
        search_results = driver.find_elements(MobileBy.CLASS_NAME, "android.widget.TextView")
        assert (len(search_results) > 0)


if __name__ == "__main__":
    pytest.main([__file__])