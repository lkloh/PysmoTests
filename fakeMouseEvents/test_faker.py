import unittest
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from faker import SetUp

class FakerTests(unittest.TestCase):

	def testMatchesWeekday(self):
		m = PyMouse()
		k = PyKeyboard()
		SetUp()

		result = k.press_key('H')
		print result
		self.assertTrue(1==1)

def main():
	unittest.main()

if __name__ == '__main__':
	main()