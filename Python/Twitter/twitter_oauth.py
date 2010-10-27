#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

import tweepy
 
CONSUMER_KEY = 'paste your Consumer Key here'
CONSUMER_SECRET = 'paste your Consumer Secret here'
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
#Open URL in a browser, allow the request, finally get you pin
print 'Please authorize: ' + auth_url    
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret

