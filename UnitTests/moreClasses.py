import datetime

class DatePattern:

	def __init__(self, year, month, day, weekday=0):
		self.year = year
		self.month = month
		self.day = day
		self.weekday = weekday

	def matches(self,date):
		return (self.yearMatches(date) and
			self.monthMatches(date) and
			self.dayMatches(date) and
			self.weekdayMatches(date))

	def yearMatches(self, date):
		if not self.year: 
			return True
		return self.year == date.year

	def monthMatches(self, date):
		if not self.month: 
			return True
		return self.month == date.month

	def dayMatches(self, date):
		if not self.day:
			return True
		return self.day == date.day

	def weekdayMatches(self, date):
		if not self.weekday:
			return True
		return self.weekday == date.weekday