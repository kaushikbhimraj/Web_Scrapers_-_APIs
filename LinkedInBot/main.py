
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Since this program is being executed from a linux env in windows, the following path needs to be specified.
# username and password are provided from a different file. 
class LinkedInBot:
	def __init__(self):

		# Login information
		self._path        = "/mnt/c/Users/kaush/Desktop/Code/03_Git_Projects/Job_Search_Web_Crawlers_202005/LinkedInBot/chromedriver.exe"
		self._json_path   = "/mnt/c/Users/kaush/Desktop/login.json"
		self._base_url    = "https://www.linkedin.com"
		self._driver      = None
		self._credentials = None
		self._username    = None
		self._password    = None

		# Job search 
		self.job_title    = "Software Engineer"
		self.location     = "United States"

	def _setDriver(self):
		self._driver     = webdriver.Chrome(self._path)
		
	def _getCredentials(self):
		with open(self._json_path) as json_file:
			self._credentials = json.load(json_file)
		json_file.close()

	def _setCredentials(self):
		self._username = self._credentials["username"]
		self._password = self._credentials["password"]
		

	# Login to your main page. 
	def _main(self):
		self._setDriver()

		# Click the Sign in button
		self._driver.get(self._base_url)
		self._driver.find_element_by_xpath("//a[contains(text(), 'Sign in')]").click()
		sleep(3)

		# Get Credentials.
		self._getCredentials()
		self._setCredentials()

		# Login using username and password. 
		self._driver.find_element_by_id("username").send_keys(self._username)
		self._driver.find_element_by_id("password").send_keys(self._password)

		# Click the sign-in button
		self._driver.find_element_by_xpath("//button[@class=\"btn__primary--large from__button--floating\"]").click()

		# Open saved job page and filter positions.
		self.Jobs()

		# Parse through the first 10 filtered positions.
		self.getJobLinks()

		return self._driver


	# Method to load the job search page after login and click on specific save job searches. 
	def Jobs(self):

		# Load the jobs pages. 
		self._driver.get(self._base_url + "/jobs/")
		sleep(5)

		# Enter job title in the keyword tab.
		self._driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-keyword-id-')]").click()
		self._driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-keyword-id-')]").send_keys(self.job_title)

		# Enter location in locations tab.
		self._driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-location-id-')]").click()
		self._driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-location-id-')]").send_keys(self.location)

		# Click the search button. 
		self._driver.find_element_by_xpath("//button[@class=\"jobs-search-box__submit-button artdeco-button artdeco-button--3 ml2\"]").click()
		sleep(5)

		# After the job page loads, click on the 'All Filers' button. 
		# This will open additional settings to narrow job search. 
		self._driver.find_element_by_xpath("//button[@data-control-name=\"all_filters\"]").click()
		sleep(2)

		# Sort by: Most Recent
		self._driver.find_element_by_xpath("//input[@id=\"sortBy-DD\"]").send_keys(Keys.SPACE)
		
		# Job Type: Full-Time 
		self._driver.find_element_by_xpath("//input[@id=\"jobType-F\"]").send_keys(Keys.SPACE)

		# Select all companies in list. 
		print("\n")
		FAANG = ["Google", "Microsoft", "Netflix", "Amazon", "Facebook", "Twitter", "Reddit", "eBay", "LinkedIn"]
		print("Searching jobs in the following companies...")
		for company in FAANG:
			self._driver.find_element_by_xpath("//input[contains(@placeholder, 'Add a company')]").click()
			self._driver.find_element_by_xpath("//input[contains(@placeholder, 'Add a company')]").send_keys(company)
			sleep(3)
			self._driver.find_element_by_xpath("//input[contains(@placeholder, 'Add a company')]").send_keys(Keys.ENTER)
			print(company)
		
		# Experience Level: Entry-Level / Associates Level
		self._driver.find_element_by_xpath("//input[@id=\"experience-2\"]").send_keys(Keys.SPACE)
		self._driver.find_element_by_xpath("//input[@id=\"experience-3\"]").send_keys(Keys.SPACE)
		sleep(2)
		
		# Click 'Apply'.
		self._driver.find_element_by_xpath("//button[@class=\"search-advanced-facets__button--apply ml4 mr2 artdeco-button artdeco-button--3 artdeco-button--primary ember-view\"]").click()
		sleep(2)

		print("Sucessfully created filter for job search!")
		print("\n")

	
	def getJobLinks(self):
		print("Fetching links for your job positions...")
		job_buttons = self._driver.find_elements_by_xpath("//a[@class=\"disabled ember-view job-card-container__link job-card-list__title\"]")
		for job_button in job_buttons:
			print(type(job_button))



			
	# Save the text scraped from the HTML to file/JSON on disk.
	def saveToFile(self):
		pass

# Run
x = LinkedInBot()._main()