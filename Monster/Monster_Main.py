# Main program for the application.
from Monster_JobSearch import Monster_JobSearch

jobTitle   = input("Enter Job Title to search:       ")
city       = input("Enter your city of search:       ")
state      = input("Enter you state of search:       ")
postedDate = input("Posting date within (# of days): ")

Monster_JobSearch().getInfo(jobTitle, city, state, postedDate)
