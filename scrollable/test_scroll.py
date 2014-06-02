from matplotlib.pyplot import *

class SetUp:

	def __init__(self):
		self.axes = self.getAxes()

	def getAxes(self):
		fig = figure(figsize=(10,10))
		self.fig = fig

		# allocate size of buttons
		space = 0.10
		axs = {}
		for i in range(10):
			recti = [0.05, space*i, 0.10, 0.08]
			self.fig.add_axes(recti)

		show()

def main():
	setup = SetUp()

if __name__ == "__main__":
	main()