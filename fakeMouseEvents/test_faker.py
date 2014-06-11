import unittest
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from faker import SetUp
import matplotlib.pyplot as py

class AcceptanceTests(unittest.TestCase):

	def testMatchesWeekday(self):
		m = PyMouse()
		k = PyKeyboard()
		instance = SetUp()
		result = SetUp.addStuff(instance, 3,4)
		print result
		k.press_key('H')
		py.close()
		self.assertTrue(1==1)

def main():
	unittest.main()

if __name__ == '__main__':
	main()