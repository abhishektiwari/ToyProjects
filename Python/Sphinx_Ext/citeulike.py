# -*- coding: utf-8 -*-
"""
    sphinx.ext.citeulike
    ~~~~~~~~~~~~~~~~~~~~
    Allows to insert citation from CiteULike 

    Abhishek Tiwari, abhishek@abhishek-tiwari.com, 3-clause BSD license.

"""

from docutils import nodes
from sphinx.util.compat import Directive
from sphinx.util.compat import make_admonition


class citeulike(nodes.Admonition, nodes.Element):
    pass

class citeulikelist(nodes.General, nodes.Element):
    pass

def visit_citeulike_node(self, node):
    self.visit_admonition(node)

def depart_citeulike_node(self, node):
    self.depart_admonition(node)



class citeulikelistDirective(Directive):

    def run(self):
        return [citeulikelist('')]

class citeulikeDirective(Directive):

    # this enables content in the directive
    has_content = True

    def run(self):
        env = self.state.document.settings.env

        targetid = "citeulike-%d" % env.new_serialno('citeulike')
        targetnode = nodes.target('', '', ids=[targetid])

        ad = make_admonition(citeulike, self.name, [_('citeulike')], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        if not hasattr(env, 'citeulike_all_citeulikes'):
            env.citeulike_all_citeulikes = []
        env.citeulike_all_citeulikes.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'citeulike': ad[0].deepcopy(),
            'target': targetnode,
        })

        return [targetnode] + ad

def purge_citeulikes(app, env, docname):
    if not hasattr(env, 'citeulike_all_citeulikes'):
        return
    env.citeulike_all_citeulikes = [citeulike for citeulike in env.citeulike_all_citeulikes
                          if citeulike['docname'] != docname]


def process_citeulike_nodes(app, doctree, fromdocname):
    if not app.config.citeulike_include_citeulikes:
        for node in doctree.traverse(citeulike):
            node.parent.remove(node)

    # Replace all citeulikelist nodes with a list of the collected citeulikes.
    # Augment each citeulike with a backlink to the original location.
    env = app.builder.env

    for node in doctree.traverse(citeulikelist):
        if not app.config.citeulike_include_citeulikes:
            node.replace_self([])
            continue

        content = []

        for citeulike_info in env.citeulike_all_citeulikes:
            para = nodes.paragraph()
            filename = env.doc2path(citeulike_info['docname'], base=None)
            description = (
                _('(The original entry is located in %s, line %d and can be found ') %
                (filename, citeulike_info['lineno']))
            para += nodes.Text(description, description)

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(_('here'), _('here'))
            newnode['refdocname'] = citeulike_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, citeulike_info['docname'])
            newnode['refuri'] += '#' + citeulike_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para += nodes.Text('.)', '.)')

            # Insert into the citeulikelist
            content.append(citeulike_info['citeulike'])
            content.append(para)

        node.replace_self(content)



def setup(app):
    app.add_config_value('citeulike_include_citeulikes', False, False)

    app.add_node(citeulikelist)
    app.add_node(citeulike,
                 html=(visit_citeulike_node, depart_citeulike_node),
                 latex=(visit_citeulike_node, depart_citeulike_node),
                 text=(visit_citeulike_node, depart_citeulike_node))

    app.add_directive('citeulike', citeulikeDirective)
    app.add_directive('citeulikelist', citeulikelistDirective)
    app.connect('doctree-resolved', process_citeulike_nodes)
    app.connect('env-purge-doc', purge_citeulikes)
