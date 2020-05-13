import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from Monster_ValidationChecks import Checks
from Monster_Extract_Key_Words import JobProcess


class Monster_JobSearch(JobProcess):
	"""
	returns HTML content for an URL request. 

	__init__(self):
					loads a dictionary object
					loads a static search URL: https://www.monster.com/jobs/search/Full-Time_8?

	getInfo: 		scraps job information from a returned HTML request
	"""
	def __init__(self):
		self.link = "https://www.monster.com/jobs/search/Full-Time_8?"


	def getInfo(self, jobTitle=None, city=None, state=None, postedDate=None):
		"""
		scrap job postings and related details from static HTML.
		getInfo(self, jobTitle=str, city=str, state=str, postedDate=int)
		"""

		paramsLink 		= self.link + self._queryParameters(jobTitle, city, state, postedDate)
		page 			= requests.get(paramsLink)
		
		# Request info
		print("\n")
		print("QUERY LINK:")
		print(paramsLink)
		print("\n")
		print("STATUS CODE:")
		print(page.status_code)
		print("\n")

		# Checking for request errors.
		if page.status_code == 404:
			raise Exception("Please check link: " + self.link)

		# Fetching data using HTML tags.
		soupPage 		= BeautifulSoup(page.content, "html.parser")
		results 		= soupPage.find(id="ResultsContainer")
		jobResults 		= results.find_all("section", class_="card-content")
<<<<<<< HEAD
		jobCount 		= 0

		# Running through each job in list. 
		# There are some sections that do not have a hyperlink.
		for jobResult in jobResults:
			jobHyperLink = jobResult.find("a")

			if jobHyperLink is not None:
				jobCount += 1

				jobId 	 = jobResult['data-jobid']
				jobTitle = jobResult.find("h2", class_="title").text.strip()
				company  = jobResult.find("div", class_="company").text.strip()
				hrefLink = jobHyperLink["href"]
				temp     = self._getDetails(hrefLink)

				# Request details from each job link.
				self.jobDictionary[jobId] = {"jobTitle":jobTitle,"company":company,"href":hrefLink,"jobDetails":temp, "dateAdded":str(datetime.now().date())}
=======
		
		# Output a json format.
<<<<<<< HEAD
		print(json.dumps(self.getResults(jobResults), indent=4))
>>>>>>> job_details_2020_10_03
=======
		fileName 		= "Monster_JobSearch_" + datetime.today().strftime("%Y-%m-%d-%H_%M_%S") + ".json"
		with open(fileName, "w") as outfile:
			json.dump(self.getResults(jobResults), outfile)
			outfile.close()

		print("JOB FETCHING COMPLETE:")
		print("created " + fileName)
>>>>>>> job_details_2020_10_03


	def _queryParameters(self, jobTitle, city, state, postedDate):
		"""
		Build query for search URL. (Internal)
		_queryParameters(self, jobTitle=str, city=str, state=str, postedDate=int)
		"""

		check = Checks()
		check.checkStrValType_Helper(jobTitle)
		check.checkStrValType_Helper(city)
		check.checkStrValType_Helper(state)
		check.checkIntValType_Helper(postedDate)

		# Data manipulation for search words, city and state.
		q     = jobTitle.replace(" ","-")
		q     = q.lower()
		city  = city.split(" ")
		city  = [city[i].title() for i in range(len(city))]
		city  = " ".join(city)
		where = check.stringConv_Helper(city) + "__2C-" + check.stringConv_Helper(state.upper())
		tm    = str(postedDate)

<<<<<<< HEAD
		return "q=" + q + "&where=" + where +"&tm=" + tm + "&stpage=1&page=2"
=======
		return "q=" + q + "&where=" + where +"&tm=" + tm
<<<<<<< HEAD


# Driver
Monster_JobSearch().getInfo("python developer", "san francisco", "ca", 14)
>>>>>>> job_details_2020_10_03
=======
>>>>>>> job_details_2020_10_03
