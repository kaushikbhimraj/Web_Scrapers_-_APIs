
import json
import requests
from datetime import date
from bs4 import BeautifulSoup


class LinkedIn_Search():

	def getJobDetails(self):
		# Open text file with link.
		try:
		    linkFile = open("/Users/kaushikbhimraj/Google Drive/Job_Links/LinkedIn_Daily " + str(date.today()) + ".txt", "r")
		    link = linkFile.read()
		except IOError:
		    print("File not accessible")
		    return 
		finally:
		    linkFile.close()

		# Load HTML from page. 
		page = requests.get(link)
		if page.status_code == 404:
			raise Exception("Oops...something went wrong!")

		# Parse contents...
		soupPage   = BeautifulSoup(page.content, "html.parser")
		results    = soupPage.find(id="main-content")
		jobResults = results.find_all("li", class_="result-card job-result-card result-card--with-hover-state")
		dumpFile   = open("/Users/kaushikbhimraj/Google Drive/Job_Search/LinkedIn_Daily " + str(date.today())+".txt", "w")

		# Extract and write job details to new file...
		dumpFile.write("Created on: " + str(date.today()) + "\n")
		dumpFile.write("\n")

		for job in jobResults:
			try:
				time = job.find("time", class_="job-result-card__listdate").text.strip()
			except AttributeError:
				time = job.find("time", class_="job-result-card__listdate--new").text.strip()

			if "days" in time or "hours" in time or "hour" in time or "day" in time:
				jobTitle = job.find("h3", class_="result-card__title job-result-card__title").text.strip()
				company  = job.find("a", class_="result-card__subtitle-link job-result-card__subtitle-link").text.strip()
				location = job.find("span", class_="job-result-card__location").text.strip()
				jobLink  = job.find("a", class_="result-card__full-card-link")["href"]
				jobDesc  = self.getJobDescription(jobLink)

				dumpFile.write("Company:         " + company + "\n")
				dumpFile.write("Job Title:       " + jobTitle + "\n")
				dumpFile.write("Elapsed Time:    " + time  + "\n")
				dumpFile.write("Location:        " + location + "\n")
				dumpFile.write("\n")
				dumpFile.write("Link:            " + jobLink + "\n")
				dumpFile.write("\n")
				dumpFile.write("Job Description: " + jobDesc + "\n")
				dumpFile.write("\n")

		dumpFile.close()
		print("File created...")

	# Helper function to acquire job details for each job listing. 
	def getJobDescription(self, jobUrl):
		jobPage = requests.get(jobUrl)

		if jobPage.status_code == 404:
			raise Exception("Oops...something went wrong!")

		soupJobPage = BeautifulSoup(jobPage.content, "html.parser")
		jobDescription = soupJobPage.find("div", class_="description__text description__text--rich").text.strip()

		return jobDescription


LinkedIn_Search().getJobDetails()
