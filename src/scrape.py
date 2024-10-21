from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

def scrape_website(website):
	print("Launching chrome browser...")
	
	chromium_remote_connection = ChromiumRemoteConnection("http://chromium:4444/wd/hub", 'goog', 'chrome')
	options = ChromeOptions()
	options.add_argument("--headless")
	with Remote(chromium_remote_connection, options=options) as driver:
		print(f"Connected! Navigating to {website}...")
		driver.get(website)

		# TODO: Captcha handling
		# print("Waiting for captcha to be solved...")
		# solve_res = driver.execute('executeCdpCommand', {
		# 	'cmd': "Captcha.waitForSolve",
		# 	"params": {"detectTimeout": 10000},
		# })
		# print("Captcha solve status: " + solve_res['value']['status'])
		# print("Navigated! Scraping page content...")
		html = driver.page_source
		return html