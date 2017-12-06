#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import csv

def multifile_concat(source_folder,output_file):
	#HOME=os.environ['HOME']
	files_to_cat = ''
	#-*- Create List of Files to Loop over. -*-#
	fList=subprocess.check_output(["ls", source_folder]).split()

	for f in fList:
		files_to_cat = files_to_cat + source_folder + "/" + f + ' '
		cmd = "cat " + files_to_cat +  " >" + output_file
	os.system(cmd)
	return cmd

def height(b,c,d): 
    I = b ** 2 - 3 * c
    J = -2 * b ** 3 + 9 * b * c - 27 * d
    return max(abs(I) ** 3, J ** 2 / 4)

def discriminant(f0, f1, f2, f3):
	disc = (f1**2 * f2**2) - (4 * f0 * f2**3) - (4 * f3 * f1**3) - (27 * f0**2 * f3**2) + (18 * f0 * f1 * f2 * f3)
	return disc

def bTranslate(J):
	if J % 3 == 0:
		return 0
	elif J % 3 == 1:
		return 1
	else:
		return -1

def modCheck(I,J):
	if I % 3 == 0 and J % 27 == 0:
		#print  0,0,I,J,I % 3, J % 27
		return True

	elif I % 9 == 1 and J % 27 == 2:
		#print  I % 9, J%27
		return True

	elif I % 9 == 1 and J % 27 == 25:
		#print  1,25,I,J,I % 9, J % 27
		return True

	elif I % 9 == 4 and J % 27 == 16:
		#print  4,16,I,J,I % 9, J % 27 
		return True

	elif I % 9 == 4 and J % 27 == 11: 
		#print  4,11,I,J,I % 9, J % 27
		return True
	
	elif I % 9 == 7 and J % 27 == 7:
		#print  7,7,I,J,I % 9, J % 27
		return True

	elif I % 9 == 7 and J % 27 == 20:
		#print  7,20,I,J,I % 9, J % 27
		return True
	
	else: 
		return False

def positive_bcf_gen(IVAL):
	
	I=IVAL[0]
	jLim=IVAL[1]
	TEMP_FOLDER=IVAL[2]
	Pos_bcfList=[]

	for J in range(-jLim, jLim+1):
		if modCheck(I,J):
			phi = bTranslate(J)
			c = (phi**2-I)/3.0
			df = ((-2.0*phi**3)/27.0)+ ((phi/9.0)*(phi**2.0-I)) - (J/27.0)
			d = round(df,0)
			disc=discriminant(1,phi,int(c),d)
			if (disc > 0):
				Pos_bcfList.append((I,J,int(height(phi,c,d)),1,phi,int(c),int(d),disc))
							
	if len(Pos_bcfList) != 0:
		FILE_NAME = TEMP_FOLDER + str(I)
		with open(FILE_NAME,'wb') as out:
    			csv_out=csv.writer(out)
    			for row in Pos_bcfList:
        			csv_out.writerow(row)	
		out.close()

