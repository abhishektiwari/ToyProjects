# -*- coding: utf-8 -*-
"""
    sphinx.ext.citelinks
    ~~~~~~~~~~~~~~~~~~~

    Extension to add CiteULike, Pubmed and DOI citation in the reST documents.

    This adds a new config value called ``citelinks`` that is created like this::

    citelinks = {'cite': ('http://www.citeulike.org/user/abhishek_tiwari/article/%s','citeulike'),
		 'doi': ('http://dx.doi.org/%s','doi'), 
		 'pubmed': ('http://www.ncbi.nlm.nih.gov/pubmed/%s','pubmed')}

    Now you can use e.g. 
       :cite:`8246763`
       :doi:`10.1016/B978-019517720-6.50016-X`
       :pubmed:`18713453` 
    in your documents.  
    
    This will create a link to
       http://www.citeulike.org/user/abhishek_tiwari/article/8246763
       http://dx.doi.org/10.1016/B978-019517720-6.50016-X
       http://www.ncbi.nlm.nih.gov/pubmed/18713453

    The link caption depends on the document type generated *prefix* value given:

    - In HTML docs prefix is not used, and references will be automatically numbered
    - In Latex docs prefix is used to generate citation tags like
       \cite{citeulike:8246763}

    You can also give an explicit caption, e.g. 
       :cite:`Polypharmacology Directed Compound Data Mining <8246763>` 

    :copyright: Copyright 2010 by Abhishek Tiwari.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes, utils

from sphinx.util.nodes import split_explicit_title

refnumber = 1

def make_link_role(base_url, prefix):
    def role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
        text = utils.unescape(text)
        has_explicit_title, title, part = split_explicit_title(text)
	refno = 1
        try:
            full_url = base_url % part
        except (TypeError, ValueError):
            env = inliner.document.settings.env
            env.warn(env.docname, 'unable to expand %s extlink with base '
                     'URL %r, please make sure the base contains \'%%s\' '
                     'exactly once' % (typ, base_url))
            full_url = base_url + part
        if not has_explicit_title:
		global refnumber 
		title = "[" + str(refnumber) + "]"	
		refnumber += 1                
                latex_title = prefix + ":" + part 

        pnode = nodes.reference(title, title, internal=False, refuri=full_url)
        return [pnode], []
    return role

def setup_link_roles(app):
    for name, (base_url, prefix) in app.config.citelinks.iteritems():
        app.add_role(name, make_link_role(base_url, prefix))

def setup(app):
    app.add_config_value('citelinks', {}, 'env')
    app.connect('builder-inited', setup_link_roles)
