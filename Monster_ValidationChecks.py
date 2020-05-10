

class Checks:

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