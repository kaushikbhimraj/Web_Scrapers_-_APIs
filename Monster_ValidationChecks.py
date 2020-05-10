class Checks:
	"""
	validate and replace strings
	validate integers 
	
	stringConv_Helper(self, string): 			
		replaces blank spaces with "-". 

	checkStrValType_Helper(self, int): 
		checks value to raise TypeError and ValueError for string inputs.

	checkIntValType_Helper(self, string):
		checks value to raise TypeError and ValueError for integer inputs. 

	"""
	def stringConv_Helper(self, stringValue):
		return stringValue.replace(" ","-")


	def checkStrValType_Helper(self, stringValue):
		if type(stringValue) != str or not stringValue:
			raise TypeError("Value was not a string.")


	def checkIntValType_Helper(self, intValue):
		if intValue < 0:
			raise ValueError("Value should be above 0.")

		if type(intValue) != int:
			raise TypeError("Value was not an integer.")