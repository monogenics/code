#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-*--------------------------------------------------------------------------------------------------------------*-#
#-*- p-gen-bcf.py: generate postive bcfs. This is done using parallel processing since the positive		-*-#
#-*- generated bcfs are already ordered by height. This program generates a set of files that are placed	-*-#
#-*- under TEMP_FOLDER. Each file in the folder corresponds to the outermost loop I. Finally, concat values.	-*-#
#-*--------------------------------------------------------------------------------------------------------------*-#

import os
import sys
import math
import multiprocessing as mp
import helper_functions as hp

#--- Pass command line valie for Y, processors, and TEMP_FOLDER ---#
try:
	Y = float(sys.argv[1])
	NUM_PROC = int(sys.argv[2])
	TEMP_FOLDER = sys.argv[3]
except IndexError:
	print "Usage: ./p-gen-bcf <Y> <processors> <TEMP_FOLDER>"
	sys.exit(1)

#--- Clean up, incase there are left over files ---#
cmd = 'rm ' + TEMP_FOLDER + '/*'
os.system(cmd)

#--- Calculate loop & range values ---#
iLim = int(math.floor(Y**(1.0/3.0)))
jLim = int(math.floor(2*Y**(1.0/2.0)))
I =  range(-iLim, iLim+1)

#--- Create value for parallel processing ---#
I2=[]
for i in I:
	value=i,jLim,TEMP_FOLDER
	I2.append(value)

#--- Call parallel processing  ---#
pool = mp.Pool(NUM_PROC)
results = pool.map(hp.positive_bcf_gen, I2)

#-* Concatenate files into single file -*-#
RESULT_FILE = str(int(Y)) + '.txt'
hp.multifile_concat(TEMP_FOLDER,RESULT_FILE)


