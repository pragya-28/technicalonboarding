import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from creds import BROWSERSTACK_EMAIL, BROWSERSTACK_PWD


capabilities = [
{
    "browserName": "firefox",
    "platformName": "mac"
},
{
    "browserName": "chrome",
    "platformName": "mac"
},
{
    "browserName": "safari",
    "platformName": "mac"
}
]

for capability in capabilities:
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=capability)

    wait = WebDriverWait(driver, 10)

    driver.get("https://www.browserstack.com/users/sign_in")

    email_field = wait.until(EC.visibility_of_element_located((By.ID, "user_email_login")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "user_password")))

    email_field.send_keys(BROWSERSTACK_EMAIL)
    password_field.send_keys(BROWSERSTACK_PWD)
    password_field.send_keys(Keys.RETURN)

    wait.until(EC.url_contains("dashboard"))
    time.sleep(3)

    browser_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='accordion__header os-section__list os-section__list--windows-icon ']//div[@class='os-section__accordion-header']")))
    browser_icon.click()

    edge_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Windows 11']")))
    edge_icon.click()

    run_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='edge 114 beta']")))
    run_button.click()
    time.sleep(20)

    driver.quit()
    time.sleep(5)