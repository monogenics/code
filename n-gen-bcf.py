#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import math
import sys
import helper_functions as hp

#-*- Pass Y value - this is not parallelized because sort is required *-#
try:
	Y = float(sys.argv[1])
except IndexError:
	print "Usage: <Y>"
	sys.exit(1)

bcfList=[]
iLim = int(math.floor(Y**(1.0/3.0)))
jLim = int(math.floor(2*Y**(1.0/2.0)))

for I in range(-iLim, iLim+1): 
	for J in range(-jLim, jLim+1):	
		if hp.modCheck(I,J):
			phi = hp.bTranslate(J)
			c = (phi**2-I)/3.0
			df = ((-2.0*phi**3)/27.0)+ ((phi/9.0)*(phi**2.0-I)) - (J/27.0)
			d = round(df,0)
			disc=hp.discriminant(1,phi,int(c),d)
			if (disc < 0):
				bcfList.append((I,J,int(hp.height(phi,c,d)),1,phi,int(c),int(d),disc))

if len(bcfList) != 0:
		FILE_NAME = str(int(Y)) + ".txt"
		with open(FILE_NAME,'wb') as out:
    			csv_out=csv.writer(out)
    			for row in sorted(bcfList, key=lambda bcf: bcf[2]):
        			csv_out.writerow(row)	
		out.close()
