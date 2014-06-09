import datetime

class DatePattern:

	def __init__(self, year, month, day):
		self.date = datetime.date(year, month, day)

	def matches(self, date):
		return self.date == date