import unittest

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from faker import SetUp
import matplotlib.pyplot as py
import Tkinter as tk

instance = SetUp()

class AcceptanceTests(unittest.TestCase):

	def test_keyEvent(self):	
		fake_event = matplotlib.backend_bases.Event('KeyEvent', instance.fig)
		fake_event.key = 'H'
		SetUp.on_key(instance, fake_event)

	def test_clickingTextingBtn(self):
		fake_event = matplotlib.backend_bases.MouseEvent('button_press_event', instance.fig.canvas, 123, 129)
		if instance.bntext.label.get_text() == 'Text':
			SetUp.texting(instance, fake_event)
			self.assertTrue(instance.bntext.label.get_text(),'LOL')
		else:
			SetUp.texting(instance, fake_event)
			self.assertTrue(instance.bntext.label.get_text(),'Text')

	def test_radioBtn(self):
		self.assertNotEqual(instance.bnBandLabel.label.get_text(), 'high')

		SetUp.getBand(instance, 'high')
		self.assertEqual(instance.bnBandLabel.label.get_text(), 'high')

def main():
	unittest.main()

if __name__ == '__main__':
	main()
	py.close('all')