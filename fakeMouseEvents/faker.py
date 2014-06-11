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

		self.bntext = py.Button(self.axs['text'], 'Text')
		self.cidtext = self.bntext.on_clicked(self.texting)

		self.bnchange= py.Button(self.axs['change'], 'Change')
		self.cidchange = self.bnchange.on_clicked(self.changed)

		cidpress = self.fig.canvas.mpl_connect('key_press_event', self.on_key)

		py.show()

	def on_key(self, event):
		print 'YOLOSWAG'

	def texting(self, event):
		print self.bntext.label.get_text()
		if self.bntext.label.get_text() == 'Text':
			self.bntext.label.set_text('LOL')
		else:
			self.bntext.label.set_text('Text')

	def addAxes(self):
		axs = {}
		rectchange = [0.20, 0.50, 0.20, 0.05]
		axs['change'] = self.fig.add_axes(rectchange)
		recttext = [0.20, 0.30, 0.20, 0.05]
		axs['text'] = self.fig.add_axes(recttext)
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