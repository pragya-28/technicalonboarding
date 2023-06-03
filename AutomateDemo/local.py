import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from creds import BROWSERSTACK_EMAIL, BROWSERSTACK_PWD

def get_driver(browser):
	if browser == 'chrome':
		return webdriver.Chrome()
	if browser == 'firefox':
		return webdriver.Firefox()
	if browser == 'safari':
		return webdriver.Safari(executable_path='/usr/bin/safaridriver')

for browser_type in ['chrome','firefox','safari']:
	try:
		driver = get_driver(browser_type)
		wait = WebDriverWait(driver, 10)
		driver.maximize_window()
		driver.get("https://www.browserstack.com/users/sign_in")

		email_field = wait.until(EC.visibility_of_element_located((By.ID, "user_email_login")))
		password_field = wait.until(EC.visibility_of_element_located((By.ID, "user_password")))

		email_field.send_keys(BROWSERSTACK_EMAIL)
		time.sleep(3)
		password_field.send_keys(BROWSERSTACK_PWD)
		time.sleep(3)
		password_field.send_keys(Keys.RETURN)

		wait.until(EC.url_contains("dashboard"))
		time.sleep(5)
	
		browser_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='accordion__header os-section__list os-section__list--windows-icon ']//div[@class='os-section__accordion-header']")))
		browser_icon.click()
		time.sleep(5)

		edge_icon = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Windows 11']")))
		edge_icon.click()
		time.sleep(5)

		run_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='edge 114 beta']")))
		run_button.click()
		time.sleep(30)
		
		driver.quit()
		time.sleep(5)
	except Exception as e:
		print(f"Error - {e}")