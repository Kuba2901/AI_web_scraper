from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def scrape_website(website):
	print("Launching chrome browser...")
	options = webdriver.ChromeOptions()
	driver = webdriver.Remote("http://chromium:4444/wd/hub", options=options)

	try:
		driver.get(website)
		print("Page loaded...")
		html = driver.page_source

		return html
	finally:
		driver.quit()
