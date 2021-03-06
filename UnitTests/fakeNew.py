import unittest
from moreClasses import DatePattern
import datetime

class FooTests(unittest.TestCase):

	def testMatchesFalse(self):
		p = DatePattern(2014, 9, 28)
		d = datetime.date(2014, 9, 29)
		self.failIf(p.matches(d))

	def testMatchesTrue(self):
		p = DatePattern(2014, 9, 28)
		d = datetime.date(2014, 9, 28)
		self.failUnless(p.matches(d))

	def testMatchesYearAsWildCard(self):
		p = DatePattern(0, 4, 10)
		d = datetime.date(2005, 4, 10)
		self.failUnless(p.matches(d))

	def testMatchesYearAndMonthAsWildcards(self):
		p = DatePattern(0,0,1)
		d = datetime.date(2004,10,1)
		self.failUnless(p.matches(d))

	def testMatchesWeekday(self):
		p = DatePattern(0,0,0,2) #2 is wednesday
		d = datetime.date(2004,9,29)
		self.failUnless(p.matches(d))

def main():
	unittest.main()

if __name__ == '__main__':
	main()