#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

import urllib2
import simplejson as json

#myurl = "http://www.citeulike.org/json/user/abhishek_tiwari/article/8246763"
myurl = "http://www.citeulike.org/json/user/abhishek_tiwari/article/747040"
myjson = urllib2.build_opener().open(myurl).read()
jdictionary = json.loads(myjson)[0]
keys = jdictionary.keys()
values = jdictionary.values()
noauthors = len (jdictionary['authors'])
authorlist = ""
for i in range(0, noauthors):
	if i == 0:
		authorlist = authorlist + jdictionary['authors'][i] 
	else:
		authorlist = authorlist + ", " + jdictionary['authors'][i]
	
citation = authorlist + ". " +  str(jdictionary['title']) + ", " + str(jdictionary['journal']) + ", " + str(jdictionary['published'][0]) + "."
print citation
