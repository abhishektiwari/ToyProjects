#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

# The New-FIX format is defined by a header and then two or more data 
# lines. The header must start with "@$" and the rest of the line is 
# treated as a comment. The data lines are four numbers separated by 
# valid separators (i.e., tab, space, comma). The four order specific
# numbers are the hormone concentration, an estimate of the precision
# of the hormone concentration, the time value, and the number of 
# sample replicates. Missing values are indicated by a zero in the 
# fourth column.

# VisPulse need input time series of 145 time points. Our time series 
# is small (nearly 60 data points), so padding the rest of our time 
# series with the last sample value, so that it is 145 in length.

import os

def fix2csv(dir, fix_file):
	"""
	Read a FIX file and convert into csv file
	"""
	with open(os.path.join(dir,fix_file), 'r') as ifile_object:
		file_content = ifile_object.readlines()
	csv_ext = ".csv"
	with open(os.path.join(dir,fix_file+csv_ext), 'w') as ofile_object:
		for index, line in enumerate(file_content):
			if line.startswith("@$"):
				pass
			else:
				value = line.split('\t')[0]
				if index == len(file_content)-1:
					padding = index
					while padding <= 145:
						print >> ofile_object, value
						padding += 1
				else:
					print >> ofile_object, value

directory = "/home/abhishek/Dropbox/MyShareLab/HTS Data/Cortisol"
# directory = raw_input('Enter directory containing FIX files? ')
extension = ".fix"
list_of_files = [file for file in os.listdir(directory) if file.lower().endswith(extension)]
for each_file in list_of_files:
	fix2csv(directory, each_file)
