import datetime

class DatePattern:

	def __init__(self, year, month, day, weekday=0):
		self.year = year
		self.month = month
		self.day = day
		self.weekday = weekday

	def matches(self, date):
		return ((self.year and self.year == date.year or True) and
			(self.month and self.month == date.month or True) and
			(self.day and self.day == date.day or True) and
			(self.weekday and self.weekday == date.weekday or True))