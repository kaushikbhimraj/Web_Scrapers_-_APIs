from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from Monster_ValidationChecks import Checks
from Monster_JobDetails import Monster_JobDetails


class JobProcess(Monster_JobDetails):
	"""
	returns a dictionary of company name, job role, job description and all the key-words. 
	getResults(self, <class bs4 object>)
					iterates through the object to extract job details from each posting in the query set. 
	_extractKeyWords(self, str)
					will tokenize the str value, creates tags for each token and returns a dictionary of key words. 
	"""

	def getResults(self, jobResultObj):
		mainCache = {}
		jobCount  = 0

		for jobResult in jobResultObj:
			jobHyperLink = jobResult.find("a")

			if jobHyperLink is not None:
				jobCount += 1

				# Scraping
				jobId 	 = jobResult['data-jobid']
				jobTitle = jobResult.find("h2", class_="title").text.strip()
				company  = jobResult.find("div", class_="company").text.strip()
				hrefLink = jobHyperLink["href"]
				
				# Making sure whether the HTML tags are in place. 
				Checks().checkStrValType_Helper(jobId)
				Checks().checkStrValType_Helper(jobTitle)
				Checks().checkStrValType_Helper(company)
				Checks().checkStrValType_Helper(hrefLink)

				jobDesc  = self._getDetails(hrefLink)
				Checks().checkStrValType_Helper(jobDesc)
				
				keyWords = self._extractKeyWords(jobDesc)
				mainCache[jobId] = {"Company":company, "Job Title":jobTitle, "Job Details":jobDesc, "KeyWords":keyWords}

		print("JOBS FOUND: ")
		print(jobCount)
		print("\n")
		return mainCache



	def _extractKeyWords(self, jobDesc):
		tempCache = {}
		
		# Tokenizing and Tagging 
		changeStrSep = jobDesc.replace("||||", ". ")
		tokens       = word_tokenize(changeStrSep)
		tags         = pos_tag(tokens, tagset="universal")

		# Organize into cache
		# Ignoring DETERMINERS, ASPOSITIONS, ADVERBS, CONJUNCTIONS
		for token in tags:
			if len(token[0]) > 1 and token[1] not in ["DET","ADP","ADV","CONJ","PRON"]:
				try:
					tempCache[token[1]]
					try:
						tempCache[token[1]][token[0]]
					except KeyError:
						tempCache[token[1]][token[0]] = token[0]
				except KeyError:
					tempCache[token[1]] = {}

		return tempCache