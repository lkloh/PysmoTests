import matplotlib, sys
matplotlib.use('TkAgg')


# Qt4Agg
from numpy import arange, sin, pi
import matplotlib.pyplot as py
from matplotlib.widgets import RadioButtons, SpanSelector
# http://stackoverflow.com/questions/23167424/matplotlib-button-color-updates-only-after-moving-mouse

class SetUp:

	def __init__(self):
		fig = self.setFigure()
		self.connect()
		py.show()

	def connect(self):
		def onselect(xmin, xmax):
			print 'LOL'
		span = SpanSelector(self.subpy, onselect, 'horizontal')

	def setFigure(self):
		fig = py.figure(figsize=(5,5))
		axs = self.addAxes(fig)
		self.axs = axs
		return fig

	def addAxes(self, fig):
		axs = {}

		#span
		self.subpy = py.subplot(111)
		self.subpy.plot([1,2,3,4,5],[6,7,8,9,10])

		return axs

def main():
	setup = SetUp()


if __name__ == "__main__":
	main()