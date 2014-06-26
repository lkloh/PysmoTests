#!/usr/bin/env python
"""
File: mccc2delay.py

Convert MCCC derived relative delay times to real delay times.
Works with multiple input files.

Input : *.mc files
Output: *.sx files for S.
  Each MCCC line is relative delay time.
  First line after that contains absolut delay time:  mean(obstt) - mean(prett).
19600102.03214806.mc --> 19600102.03214806.sx

Call getime to calculate theoretical 1d travel time.
	time, elcr, dtdd = getime(phase, slat, slon, elat, elon, edep, 0, 0, 1)
Input lat/lon are in geographic coordinate.


#######
Require phase and PDE info from MCCC output, which replace command-line input and file 'event.list'.

Need to do:
	options of elevation and crust correction. 

	
xlou 04/30/2011
"""

from numpy import *
import os, sys
from lib import lol
from lib import getime

print 'HELLO WORLD'
