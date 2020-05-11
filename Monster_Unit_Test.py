
from Monster_JobSearch import Monster_JobSearch
import unittest

class Monster_JobSearch_Test(unittest.TestCase):


	def test_getInfo(self):
		testObj = Monster_JobSearch()
		self.assertRaises(TypeError, testObj.getInfo, "software developer python", "", "ny", 12)
		self.assertRaises(TypeError, testObj.getInfo, "software developer python", "new york", "", 12)
		self.assertRaises(TypeError, testObj.getInfo, "", "new york", "ny", 12)

		self.assertRaises(TypeError, testObj.getInfo, "software developer python", "new york", 10, 12)
		self.assertRaises(TypeError, testObj.getInfo, "software developer python", 10, "ny", 12)
		self.assertRaises(TypeError, testObj.getInfo, 10, "new york", "ny", 12)

		self.assertRaises(ValueError, testObj.getInfo, "software developer python", "new york", "ny", -2)

		self.assertRaises(TypeError, testObj.getInfo, "software developer python", "new york", "ny", 1.24)
		self.assertRaises(TypeError, testObj.getInfo, "software developer python", "new york", "ny", "abc")


if __name__ == "__main__":
	unittest.main()