import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
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
				jobId 	 = jobResult['data-jobid']
				Checks().checkStrValType_Helper(jobId)
						
				jobTitle = jobResult.find("h2", class_="title").text.strip()
				Checks().checkStrValType_Helper(jobTitle)

				company  = jobResult.find("div", class_="company").text.strip()
				Checks().checkStrValType_Helper(company)

				hrefLink = jobHyperLink["href"]
				Checks().checkStrValType_Helper(hrefLink)

				jobDesc  = self._getDetails(hrefLink)
				Checks().checkStrValType_Helper(jobDesc)

				keyWords = self._extractKeyWords(jobDesc)
				mainCache[jobId] = {"Company":company, "Job Title":jobTitle, "Job Details":jobDesc, "KeyWords":keyWords}

		print("Number of Jobs found: ", jobCount)
		return mainCache



	def _extractKeyWords(self, jobDesc):
		tempCache = {}
		newTokens = []
		
		changeStrSep = jobDesc.replace("||||", ". ")
		tokens  = nltk.word_tokenize(changeStrSep)

		"""
		# Lemmetize
		sw  = stopwords.words("english")
		wnl = WordNetLemmatizer()

		while tokens:
			if tokens[0] in sw or tokens[0] in [".", ","]:
				tokens.pop(0)
			else:
				newTokens.append(wnl.lemmatize(tokens.pop(0)))
		"""

		# POS Tagging
		tags = nltk.pos_tag(tokens, tagset="universal")

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