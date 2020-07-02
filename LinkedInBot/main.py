import json
from time import sleep
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Since this program is being executed from a linux env in windows, the paths are different.
class LinkedInBot:
	def __init__(self):

		# Sleep Time
		self.short        = 3
		self.long         = 5

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

		# File Path for text files
		self.saveTo       = "/mnt/c/Users/kaush/Desktop/Daily_Jobs/"


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
		sleep(self.short)

		# Get Credentials.
		self._getCredentials()
		self._setCredentials()

		# Login username and password. 
		self._driver.find_element_by_id("username").send_keys(self._username)
		self._driver.find_element_by_id("password").send_keys(self._password)

		# Click the sign-in button
		self._driver.find_element_by_xpath("//button[@class=\"btn__primary--large from__button--floating\"]").click()

		# Open saved job page and filter positions.
		self.Jobs()

		# Parse through the first 10 filtered positions.
		self.getJobDetails()

		return self._driver


	# Method to load the job search page after login and click on specific save job searches. 
	def Jobs(self):

		# Load the jobs pages. 
		self._driver.get(self._base_url + "/jobs/")
		sleep(self.long)

		# Enter job title in the keyword tab.
		self._driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-keyword-id-')]").click()
		self._driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-keyword-id-')]").send_keys(self.job_title)

		# Enter location in locations tab.
		self._driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-location-id-')]").click()
		self._driver.find_element_by_xpath("//input[contains(@id, 'jobs-search-box-location-id-')]").send_keys(self.location)

		# Click the search button. 
		self._driver.find_element_by_xpath("//button[@class=\"jobs-search-box__submit-button artdeco-button artdeco-button--3 ml2\"]").click()
		sleep(self.long)

		# After the job page loads, click on the 'All Filters' button. 
		# This will open additional settings to narrow job search. 
		self._driver.find_element_by_xpath("//button[@data-control-name=\"all_filters\"]").click()
		sleep(self.short)

		# Sort by: Most Recent
		self._driver.find_element_by_xpath("//input[@id=\"sortBy-DD\"]").send_keys(Keys.SPACE)
		
		# Job Type: Full-Time 
		self._driver.find_element_by_xpath("//input[@id=\"jobType-F\"]").send_keys(Keys.SPACE)

		# Select all companies in list. 
		# The all the companies specified are printed on screen only after it is selected in the job search filter. 
		print("\n")
		FAANG = ["Google", "Microsoft", "Netflix", "Amazon", "Facebook", "Twitter", "Reddit, Inc.", "eBay", "LinkedIn"]
		print("Searching jobs in the following companies...")
		for company in FAANG:
			self._driver.find_element_by_xpath("//input[contains(@placeholder, 'Add a company')]").click()
			self._driver.find_element_by_xpath("//input[contains(@placeholder, 'Add a company')]").send_keys(company)
			sleep(self.long)
			self._driver.find_element_by_xpath("//input[contains(@placeholder, 'Add a company')]").send_keys(Keys.ENTER)
			print(company)
		
		# Experience Level: Entry-Level / Associates Level
		self._driver.find_element_by_xpath("//input[@id=\"experience-2\"]").send_keys(Keys.SPACE)
		self._driver.find_element_by_xpath("//input[@id=\"experience-3\"]").send_keys(Keys.SPACE)
		sleep(self.short)
		
		# Click 'Apply'.
		self._driver.find_element_by_xpath("//button[@class=\"search-advanced-facets__button--apply ml4 mr2 artdeco-button artdeco-button--3 artdeco-button--primary ember-view\"]").click()
		sleep(self.short)

		print("Sucessfully created filter for job search!")
		print("\n")


	# Get the job details
	def getJobDetails(self):
		print("Saving jobs to file...")
		job_buttons = self._driver.find_elements_by_xpath("//li[contains(@class, 'occludable-update artdeco-list__item--offset-2 artdeco-list__item p0 ember-view')]")

		# Save the 10 most recent jobs. 
		index = 0
		while True:
			if index > 10:
				break

			try:
				# Scrap HTML contents for the job and save it in a text file.  
				# File name will be a combination of the company name + position name + current date. 
				job_buttons[index].click()
				job_name     = self._driver.find_element_by_xpath("//h2[@class=\"jobs-details-top-card__job-title t-20 t-black t-normal\"]").text
				company_name = self._driver.find_element_by_xpath("//a[@data-control-name=\"company_link\"]").text
				job_details  = self._driver.find_element_by_xpath("//div[@id=\"job-details\"]").text

				today = date.today()
				file  = open(self.saveTo+company_name+"_"+job_name+"_"+today.strftime("%d.%m.%Y")+".txt", "a")
				file.writelines("Company Name:    " + company_name)
				file.writelines("\n")
				file.writelines("Position:        " + job_name)
				file.writelines("\n")
				file.writelines("Job Description: ")
				file.writelines("\n")
				file.writelines("\n")
				file.writelines(job_details)
				file.close()

				# Print details for user. 
				print("Position:     ", job_name)
				print("Company Name: ", company_name)
				print("\n")
				sleep(self.long)

			except IndexError:
				break
			index += 1

		print("Jobs were saved to file...")

# Run code
x = LinkedInBot()._main()