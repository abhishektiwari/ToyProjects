#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.


from Bio import Entrez
import json

def search(keyword):
	"""
	this function takes the keyword and search in NCBI using eUtils
	"""
	Entrez.email = "Abhishek abhishek.twr@gmail.com"
	handle = Entrez.egquery(term = keyword)
	record = Entrez.read(handle)
	return json.dumps(record)
