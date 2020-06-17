import requests
from bs4 import BeautifulSoup
from Monster_ValidationChecks import Checks


class Monster_JobDetails:
	"""
	object is used to scrap a level deeper into each of the job posts scraped from the Monster_JobSearch() class. 
	"""
	def _getDetails(self, href):
		"""
		Requests page content for the specific hyperlink and extracts/separates sentences with "||||" separator. Returns single string value. 
		_getDetails(self, href=str)
		"""

		jobDetailsStr = ""	
		page 		  = requests.get(href)
		soupPage          = BeautifulSoup(page.content, "html.parser")
		jobDetails 	  = soupPage.find(class_="container job-body-container")


		# Check if the job posting still exists.
		if jobDetails:
			rawText      = jobDetails.text.strip()
			rawTextArray = rawText.split(".")

			for line in rawTextArray:
				jobDetailsStr += line + "||||"

		return jobDetailsStr
