import unittest
import matplotlib.pyplot as py
from new_one import onselect

class AcceptanceTests(unittest.TestCase):

	def test_select(self):	
		instance = onselect(2.9,3.6)

def main():
	unittest.main()

if __name__ == '__main__':
	main()
	py.close('all')