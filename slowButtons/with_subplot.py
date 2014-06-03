import matplotlib, sys
matplotlib.use('TkAgg')
# Qt4Agg
from numpy import arange, sin, pi
import matplotlib.pyplot as py
# http://stackoverflow.com/questions/23167424/matplotlib-button-color-updates-only-after-moving-mouse

class SetUp:

	def __init__(self):
		self.fig = py.figure(figsize=(5,5))

		self.axs = self.addAxes()

		# self.bntext = py.Button(self.axs['text'], 'Text')
		# self.cidtext = self.bntext.on_clicked(self.texting)

		# self.bnquit = py.Button(self.axs['change'], 'Change')
		# self.cidquit = self.bnquit.on_clicked(self.changed)

		py.show()

	def texting(self, event):
		print self.bntext.label.get_text()
		if self.bntext.label.get_text() == 'Text':
			self.bntext.label.set_text('LOL')
		else:
			self.bntext.label.set_text('Text')

	def addAxes(self):
		axs = {}
		ax1 = py.subplot2grid((2,2),(0, 0))
		axs['ax1'] = ax1
		return axs

	def changed(self,event):
		print self.bnquit.label.get_text()
		if self.bnquit.label.get_text() == 'Change':
			self.bnquit.label.set_text('Hello')
			self.bntext.label.set_text('LOL')
		else:
			self.bnquit.label.set_text('Change')
		#self.fig.canvas.draw()
		self.axs['change'].get_figure().canvas.draw()

def main():
	setup = SetUp()


if __name__ == "__main__":
	main()







