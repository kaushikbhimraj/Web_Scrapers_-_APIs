
import json
from time import sleep
from selenium import webdriver

# Since this program is being executed from a linux env in windows, the following path needs to be specified.
# username and password are provided from a different file. 
class LinkedInBot:
	def __init__(self):

		# Login information
		self._path        = "/mnt/c/Users/kaush/Desktop/Code/Git_Projects/Job_Search_Web_Crawlers_202005/LinkedInBot/chromedriver.exe"
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
		self._driver.get(self._base_url)

	def _getCredentials(self):
		with open(self._json_path) as json_file:
			self._credentials = json.load(json_file)
		json_file.close()

	def _setCredentials(self):
		self._username = self._credentials["username"]
		self._password = self._credentials["password"]
		

	# Login to your main page. 
	def Login(self):
		self._setDriver()

		# Click the Sign in button
		self._driver.find_element_by_xpath("//a[contains(text(), 'Sign in')]").click()
		sleep(4)

		# Get Credentials.
		self._getCredentials()
		self._setCredentials()

		# Login using username and password. 
		self._driver.find_element_by_id("username").send_keys(self._username)
		self._driver.find_element_by_id("password").send_keys(self._password)

		# Click the sign-in button
		self._driver.find_element_by_xpath("//button[@class=\"btn__primary--large from__button--floating\"]").click()

		# Open saved job search in page. 
		self.Jobs()
	
		return self.driver

	# Method to load the job search page after login and click on specific save job searches. 
	def Jobs(self):

		# Load the jobs pages. 
		self._driver.get(self._base_url + "/jobs/")
		sleep(4)

		# Populate the search fields before search.
		self._driver.find_element_by_id("jobs-search-box-keyword-id-ember17").send_keys(self.job_title)
		self._driver.find_element_by_id("jobs-search-box-location-id-ember17").send_keys(self.location)

		# Click search.
		self._driver.find_element_by_xpath("//button[@class=\"jobs-search-box__submit-button artdeco-button artdeco-button--3 ml2\"]").click()
		sleep(4)

		# Click on "All Filters".
		self._driver.find_element_by_xpath("//button[@class=\"search-filters-bar__all-filters flex-shrink-zero mr3 artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view\"]").click()

		# Date Posted      -> Past Week
		# Job Type         -> Full Time
		# Company          ->
		# Experience Level -> Entry Level; Associate
		self._driver.find_element_by_id("f_TPR-r604800").click()
		self._driver.find_element_by_id("f_JT-F").click()
		self._driver.find_element_by_id("f_C-1586").click()
		self._driver.find_element_by_id("f_E-2").click()
		self._driver.find_element_by_id("f_E-3").click()
	
		# Apply filter. 		
		self._driver.find_element_by_xpath("//button[@class=\"search-advanced-facets__button--apply ml4 mr2 artdeco-button artdeco-button--3 artdeco-button--primary ember-view\"]").click()		
		

# Run
x = LinkedInBot().Login()
# x.launchBrowser()