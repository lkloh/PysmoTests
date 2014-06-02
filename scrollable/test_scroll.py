import matplotlib, sys
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.pyplot import *
import Tkinter as tk

class SetUp:

	def __init__(self, master):
		self.fig = figure(figsize=(5,5))

		self.axs = self.addAxes()
		self.bnquit = tk.Button(master, text='Quit', command=self.quitProgram)
		self.bnquit.pack(fill=tk.X)

		dataPlot = FigureCanvasTkAgg(self.fig, master=master)
		dataPlot.show()
		dataPlot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

	def addAxes(self):
		axs = {}
		for i in range(10):
			recti = [0.40, i*0.10, 0.20, 0.05]
			axs['rect'+str(i)] = self.fig.add_axes(recti)
		axs['quit'] = [0.20, 0.50, 0.20, 0.05]
		return axs

	def quitProgram(self):
		sys.exit()
		
def main():
	master = tk.Tk()
	master.title("Hello World!")
	setup = SetUp(master)
	master.mainloop()


if __name__ == "__main__":
	main()
	sys.exit()