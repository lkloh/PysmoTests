import datetime

class DatePattern:

	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

	def matches(self, date):
		return ((self.year and self.year == date.year or True) and
			self.month == date.month and
			self.day == date.day)