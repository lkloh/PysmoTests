import matplotlib, sys
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.pyplot import *
from Tkinter import *

class SetUp:

	def __init__(self, master):
		self.fig = figure(figsize=(5,5))
		self.fig.add_subplot(111)
		dataPlot = FigureCanvasTkAgg(self.fig, master=master)
		dataPlot.show()
		dataPlot.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
		
def main():
	master = Tk()
	master.title("Hello World!")
	setup = SetUp(master)
	master.mainloop()
	master.destroy()


if __name__ == "__main__":
	main()
	