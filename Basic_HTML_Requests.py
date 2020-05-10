import requests
from bs4 import BeautifulSoup


class Monster_JobSearch:
	def __init__(self):
		self.link = "https://www.monster.com/jobs/search/Full-Time_8?"


	def getPage(self, jobTitle, city, state, postingDate):
		page = requests.get(self.link + self.queryParameters(jobTitle, city, state, postingDate))
		SoupPage = BeautifulSoup(page.content, "html.parser")
		print(self.link + self.queryParameters(jobTitle, city, state, postingDate))


	def queryParameters(self, jobTitle, city, state, postingDate):
		self.checkStrValType_Helper(jobTitle)
		self.checkStrValType_Helper(city)
		self.checkStrValType_Helper(state)
		self.checkIntValType_Helper(postingDate)

		q     = jobTitle.replace(" ","-")
		q     = q.lower()

		city  = city.split(" ")
		city  = [city[i].title() for i in range(len(city))]
		city  = " ".join(city)

		where = self.stringConv_Helper(city) + "__2C-" + self.stringConv_Helper(state.upper())
		tm    = str(postingDate)

		return "q=" + q + "&where=" + where +"&tm=" + tm


	def stringConv_Helper(self, stringValue):
		return stringValue.replace(" ","-")


	def checkStrValType_Helper(self, stringValue):
		if not stringValue:
			raise ValueError("Value was empty.")

		if type(stringValue) != str:
			raise TypeError("Value was not a string.")


	def checkIntValType_Helper(self, intValue):
		if intValue < 0 or not intValue:
			raise ValueError("Value should be above 0.")

		if type(intValue) != int:
			raise TypeError("Value was not an integer.")






# Driver Code
Monster_JobSearch().getPage("software developer", "new york", "ny", 12)

