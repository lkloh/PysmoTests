import unittest
from moreClasses import DatePattern
import datetime

class FooTests(unittest.TestCase):

	def testMatches(self):
		p = DatePattern(2014, 9, 28)
		d = datetime.date(2014, 9, 29)
		self.failIf(p.matches(d))

def main():
	unittest.main()

if __name__ == '__main__':
	main()