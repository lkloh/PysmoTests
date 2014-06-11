import unittest
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class FakerTests(unittest.TestCase):

	def testMatchesWeekday(self):
		m = PyMouse()
		k = PyKeyboard()
		self.assertTrue(1==1)

def main():
	unittest.main()

if __name__ == '__main__':
	main()