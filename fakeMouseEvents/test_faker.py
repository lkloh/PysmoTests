import unittest
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from faker import SetUp
import matplotlib
import matplotlib.pyplot as py
import Tkinter

m = PyMouse()
k = PyKeyboard()
instance = SetUp()

class AcceptanceTests(unittest.TestCase):

	# key event
	def test_fakeEvent(self):	
		fake_event = matplotlib.backend_bases.Event('KeyEvent', instance.fig, Tkinter.Event)
		fake_event.key = 'H'
		SetUp.on_key(instance, fake_event)

	def test_clickingTextingBtn(self):
		fake_event = matplotlib.backend_bases.MouseEvent('button_press_event', instance.fig.canvas, 123, 129)
		SetUp.texting(instance, fake_event)
		if instance.bntext.label.get_text() == 'Text':
			SetUp.texting(instance, fake_event)
			self.assertTrue(instance.bntext.label.get_text(),'LOL')
		else:
			SetUp.texting(instance, fake_event)
			self.assertTrue(instance.bntext.label.get_text(),'Text')

def main():
	unittest.main()
	py.close('all')

if __name__ == '__main__':
	main()