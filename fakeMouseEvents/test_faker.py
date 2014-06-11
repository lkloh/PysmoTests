import unittest
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from faker import SetUp
import matplotlib
import matplotlib.pyplot as py
import Tkinter

class AcceptanceTests(unittest.TestCase):

	def AtestMatchesWeekday(self):
		m = PyMouse()
		k = PyKeyboard()

		instance = SetUp()
		result = SetUp.addStuff(instance, 3,4)
		print result
		k.press_key('H')
		py.close()
		self.assertTrue(1==1)

	def test_fakeEvent(self):
		m = PyMouse()
		k = PyKeyboard()
		
		instance = SetUp()
		fake_event = matplotlib.backend_bases.Event('KeyEvent', instance.fig, Tkinter.Event)
		fake_event.key = 'H'
		SetUp.on_key(instance, fake_event)


def main():
	unittest.main()
	py.close('all')

if __name__ == '__main__':
	main()