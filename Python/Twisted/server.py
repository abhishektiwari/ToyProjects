#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.
from twisted.web import resource, server
import search

class SearchPage(resource.Resource):
	def __init__(self, keyword):
		self.keyword = keyword

	def render(self, request):
		return search.search(self.keyword) 

class SearchRoot(resource.Resource):
	def __init__(self):
		resource.Resource.__init__(self)
		self.requestedSearch = []
		self.putChild('', SearchIndexPage(self.requestedSearch))

	def render(self, request):
		# redirect /search -> /search/
		request.redirect(request.path + '/')
		return "Please use /search/ instead."

	def getChild(self, path, request):
		if path not in self.requestedSearch:
			self.requestedSearch.append(path)
		return SearchPage(path)

class SearchIndexPage(resource.Resource):
	def __init__(self, requestedSearchList):
		resource.Resource.__init__(self)
		self.requestedSearch = requestedSearchList
    
	def render(self, request):
		request.write("""
		<html>
		<head>
		<title>MolSeek Public Search</title>
		</head>
		<body>
		<h1>Search List</h1>
		To see a search, enter a url like
		<a href='cortisol'>/search/cortisol</a>. <br />
		Kewords viewed so far:
		<ul>""")
		for keword in self.requestedSearch:
			request.write(
				"<li><a href='%s'>%s</a></li>" % (keword, keword))

		request.write("""
		    </ul>
		    </body>
		    </html>
		    """)
		return ""

class HomePage(resource.Resource):
	def render(self, request):
		return """
		<html>
		<head>
		<title>MolSeek Pubmic API</title>
		</head>
        <body>
        <h1>MolSeek Public API</h1>
        <h2>For a simple Demo</h2>
        Try this:
        <ul>
          <li><a href='/search/cortisol'>Search for "cortisol"</a></li>
		</ul>
		<h2>For more details see, <a href='/search'>search page</a></h2>
		</body>
		</html>
		"""

if __name__ == "__main__":
	from twisted.internet import reactor
	root = resource.Resource()
	root.putChild('', HomePage())
	root.putChild('search', SearchRoot())
	site = server.Site(root)
	reactor.listenTCP(8000, site)
	print "Web service started, to stop it use <ctrl-c>"
	reactor.run()
	print "Web service stopped."
