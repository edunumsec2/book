from base64 import b64encode
import csv
from docutils import nodes
from docutils.parsers.rst.states import SubstitutionDef
from docutils.statemachine import ViewList
from sphinx.errors import ExtensionError
from sphinx.util.docutils import SphinxDirective, SphinxRole
from sphinx.util.nodes import nested_parse_with_titles
from myst_parser.main import to_html
import os.path

class glossary_list(nodes.General, nodes.Element):
    pass

class glossary_definition(nodes.Inline, nodes.TextElement):
    pass

def visit_glossary_definition(self, node):
    self.body.append('<span class="glossary-ref" ' + 
        'data-definition="' + b64encode(to_html(node["definition"]).encode("UTF-8")).decode("UTF-8") + '" ' +
        'data-number="' + node["number"] + '" ' +
        'data-entry-name="' + b64encode(node["entry_name"].encode("UTF-8")).decode("UTF-8") + '">')

def depart_glossary_definition(self, node):
    self.body.append('</span>')

class GlossaryListDirective(SphinxDirective):

    def run(self):
        result_nodes = []

        for entry in self.env.glossary_entries:
            container = nodes.container(is_div=True, classes=["glossary-entry"])

            target_id = 'gl-def-%s-%s' % (entry['key'], entry['number'])
            container += nodes.target('', '', ids=[target_id])

            container += nodes.strong(entry['name'], entry['name'], classes=["glossary-name"])

            view_list = ViewList()
            for line in entry['definition'].splitlines():
                view_list.append(line, "glossary.csv", 0)
            temp_node = nodes.section()
            temp_node.document = self.state.document

            nested_parse_with_titles(self.state, view_list, temp_node)
            for child in temp_node.children:
                container += child

            index_list = glossary_list('')
            index_list.glossary_index = entry['index']
            container += index_list
            result_nodes.append(container)

        return result_nodes

def load_glossary_csv(app, env, docnames):
    entries = []
    with open(os.path.normpath(os.path.join(app.srcdir, '../glossaire.csv')), newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for i, line in enumerate(csv_reader):
            entries.append({
                'key': line[0],
                'number': line[1],
                'name': line[2],
                'definition': line[3],
                'index': i,
            })

    index = {}
    for i, entry in enumerate(entries):
        if not entry['key'] in index:
            index[entry['key']] = {}
        numbered = index[entry['key']]
        if entry['number'] in numbered:
            raise ExtensionError("Duplicate entry for glossary.")
        numbered[entry['number']] = i

    env.glossary_entries = entries
    env.glossary_entries_index = index

def process_glossary_list(app, doctree, fromdocname):
    env = app.builder.env

    for node in doctree.traverse(glossary_list):
        index = node.glossary_index
        node.replace_self([nodes.Text(str(ref)) for ref in env.glossary_references.get(index, [])])

def purge_glossary_references(app, env, docname):
    if not hasattr(env, 'glossary_references'):
        return
    
    for i, refs in env.glossary_references.items():
         env.glossary_references[i] = [ref for ref in refs
                                       if ref['docname'] != docname]

def merge_glossary_references(app, env, docnames, other):
    if not hasattr(env, 'glossary_references'):
        env.glossary_references = {}
    
    if hasattr(other, 'glossary_references'):
        for i, refs in other.glossary_references.items():
            if i not in env.glossary_references:
                env.glossary_references[i] = []
            env.glossary_references[i].extend(refs)

class GlossaryRole(SphinxRole):
    def run(self):
        env = self.env
        key = self.text
        number = '1'
        display = self.text
        if '|' in key:
            [key, display] = key.split('|', 2)
        if '@' in key:
            [key, number] = key.split('@', 2)
        i = env.glossary_entries_index[key][number]
        entry = env.glossary_entries[i]

        target_id = 'gl-%s-%d' % (key, env.new_serialno('gl-' + key))
        target_node = nodes.target('', '', ids=[target_id])

        node = glossary_definition(display, display,
            definition=entry['definition'],
            entry_name=entry['name'],
            number=entry['number'],
            classes=["glossary-ref"], **self.options)

        if not hasattr(env, 'glossary_references'):
            env.glossary_references = {}
        if not i in env.glossary_references:
            env.glossary_references[i] = []
        env.glossary_references[i].append({
            'docname': env.docname,
            'lineno': self.lineno,
            'target_id': target_id,
        })

        return [target_node, node], []

def setup(app):
    app.add_node(glossary_list)
    app.add_node(glossary_definition, html=(visit_glossary_definition, depart_glossary_definition))

    app.connect('env-before-read-docs', load_glossary_csv)
    app.connect('doctree-resolved', process_glossary_list)
    app.connect('env-purge-doc', purge_glossary_references)
    app.connect('env-merge-info', merge_glossary_references)

    app.add_directive('glossaire', GlossaryListDirective)
    app.add_role('glo', GlossaryRole())

    app.add_config_value('glossary_doc', None, 'env')

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    app.add_js_file("glossary.js")
    app.add_css_file("glossary.css")

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }


