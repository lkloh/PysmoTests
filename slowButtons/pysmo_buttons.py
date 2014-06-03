import matplotlib, sys
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
import matplotlib.pyplot as py

class SetUp:

	def __init__(self):
		self.fig = py.figure(figsize=(5,5))

		self.axs = self.addAxes()
		self.bnquit = py.Button(self.axs['change'], 'Change')
		self.cidquit = self.bnquit.on_clicked(self.changed)
		py.show()

	def addAxes(self):
		axs = {}
		rectchange = [0.20, 0.50, 0.20, 0.05]
		axs['change'] = self.fig.add_axes(rectchange)
		return axs

	def changed(self,event):
		print self.bnquit.label.get_text()
		if self.bnquit.label.get_text() == 'Change':
			self.bnquit.label.set_text('Hello')
		else:
			self.bnquit.label.set_text('Change')

def main():
	setup = SetUp()


if __name__ == "__main__":
	main()