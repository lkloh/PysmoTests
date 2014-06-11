import matplotlib, sys
matplotlib.use('TkAgg')
# Qt4Agg
from numpy import arange, sin, pi
import matplotlib.pyplot as py
# http://stackoverflow.com/questions/23167424/matplotlib-button-color-updates-only-after-moving-mouse

class SetUp:

	def __init__(self):
		fig, axs = self.setFigure()
		self.fig = fig
		self.axs = axs
		self.connect()
		py.show()

	def setFigure(self):
		fig = py.figure(figsize=(5,5))
		axs = self.addAxes(fig)

		self.bntext = py.Button(axs['text'], 'Text')
		self.bnchange= py.Button(axs['change'], 'Change')
		
		return fig, axs

	def connect(self):
		self.cidtext = self.bntext.on_clicked(self.texting)
		self.cidchange = self.bnchange.on_clicked(self.changed)
		self.cidpress = self.fig.canvas.mpl_connect('key_press_event', self.on_key)

	def addStuff(self, numA, numB):
		return numA + numB

	def on_key(self, event):
		print event.key
		if (event.key == 'H'):
			print 'YOLOSWAG'

	def texting(self, event):
		print self.bntext.label.get_text()
		if self.bntext.label.get_text() == 'Text':
			self.bntext.label.set_text('LOL')
		else:
			self.bntext.label.set_text('Text')

	def addAxes(self, fig):
		axs = {}
		rectchange = [0.20, 0.50, 0.20, 0.05]
		axs['change'] = fig.add_axes(rectchange)
		recttext = [0.20, 0.30, 0.20, 0.05]
		axs['text'] = fig.add_axes(recttext)
		return axs

	def changed(self,event):
		print self.bnchange.label.get_text()
		if self.bnchange.label.get_text() == 'Change':
			self.bnchange.label.set_text('Hello')
			self.bntext.label.set_text('LOL')
		else:
			self.bnchange.label.set_text('Change')
		print type(self.axs['text'])
		event.canvas.blit(self.axs['text'].bbox)

def main():
	setup = SetUp()


if __name__ == "__main__":
	main()