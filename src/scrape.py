from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

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

def extract_body_content(html_content):
	soup = BeautifulSoup(html_content, "html.parser")
	body_content = soup.body
	if body_content:
		return str(body_content)
	return ""

def clean_body_content(body_content):
	soup = BeautifulSoup(body_content, "html.parser")
	
	for script_or_style in soup(['script', 'style']):
		script_or_style.extract()

	cleaned_content = soup.get_text(separator="\n")
	cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

	return cleaned_content