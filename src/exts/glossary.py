 
from base64 import b64encode
import csv
from docutils import nodes
from docutils.statemachine import ViewList
from sphinx.errors import ExtensionError
from sphinx.environment.adapters.toctree import TocTree
from sphinx.util.docutils import SphinxDirective, SphinxRole
from sphinx.util.nodes import nested_parse_with_titles
from sphinx.builders.latex import LaTeXBuilder
import os.path


class glossary_list(nodes.General, nodes.Element):
    pass

class glossary_reference(nodes.Inline, nodes.TextElement):
    pass

def b64(string):
    return b64encode(string.encode("UTF-8")).decode("UTF8")

def visit_glossary_reference_html(self, node):
    self.body.append('<span class="glossary-ref" ' + 
        'data-definition="' + b64(node["definition"]) + '" ' +
        'data-number="' + node["number"] + '" ' +
        ('data-glossary-uri="' + node["uri"] + '" ' if node["uri"] is not None else '') +
        'data-entry-name="' + b64(node["entry_name"]) + '">')

def depart_glossary_reference_html(self, node):
    self.body.append('</span>')

def visit_glossary_reference_latex(self, node):
    self.body.append('\glossaryterm{')


def depart_glossary_reference_latex(self, node):
    self.body.append('}')
    
def visit_glossary_list_latex(self, node):
    self.body.append('\glossarylist')


def depart_glossary_list_latex(self, node):
    pass
    

    
def _glossary_file_name(app):
    return os.path.normpath(os.path.join(
        app.srcdir, '../glossaire.csv'))

def _def_target(key, number):
    return 'gl-def-%s-%s' % (key, number)

def _parse_id(id):
    key = id
    number = '1'
    if '@' in key:
        [key, number] = key.split('@', 2)
    return key, number

def _parse_role_content(string):
    key = string
    display = string
    if '|' in key:
        [key, display] = key.split('|', 2)
    key, number = _parse_id(key)
    return key, number, display

class GlossaryDefDirective(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    has_content = False

    def run(self):
        env = self.env
        env.note_dependency(_glossary_file_name(env.app))
        key, number = _parse_id(self.arguments[0])

        i = self.env.glossary_entries_index[key][number]
        entry = self.env.glossary_entries[i]

        adm_node = nodes.admonition('')
        adm_node += nodes.title(entry['name'], entry['name'])

        target_id = 'gl-%s-%d' % (key, env.new_serialno('gl-' + key))
        adm_node += nodes.target('', '', ids=[target_id])

        view_list = ViewList()
        for line in entry['definition'].splitlines():
            view_list.append(line, "glossaire.csv", 0)
        nested_parse_with_titles(self.state, view_list, adm_node)

        if not hasattr(env, 'glossary_references'):
            env.glossary_references = {}
        if not i in env.glossary_references:
            env.glossary_references[i] = []
        env.glossary_references[i].append({
            'type': 'DEF',
            'docname': env.docname,
            'lineno': self.lineno,
            'target_id': target_id,
        })

        return [adm_node]

class GlossaryListDirective(SphinxDirective):

    def run(self):
        self.env.note_reread()
        result_nodes = []

        for entry in self.env.glossary_entries:
            container = nodes.container(is_div=True, classes=["glossary-entry"])

            target_id = _def_target(entry['key'], entry['number'])
            container += nodes.target('', '', ids=[target_id])

            container += nodes.strong(entry['name'], entry['name'],
                                      classes=["glossary-name"])

            view_list = ViewList()
            for line in entry['definition'].splitlines():
                view_list.append(line, "glossaire.csv", 0)
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
    with open(_glossary_file_name(app), newline='', encoding='utf-8') as csv_file:
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
            raise ExtensionError("Duplicate entry for glossary: " + entry['key'])
        numbered[entry['number']] = i

    env.glossary_entries = entries
    env.glossary_entries_index = index

def index_link_node(app, fromdocname, refs):
    toc = TocTree(app.env)
    par_nodes = []
    labels = {
        'DEF': 'Définitions:',
        'USE': 'Usages:',
    }
    for type in ['DEF', 'USE']:
        relevant_refs = [ref for ref in refs if ref['type'] == type]
        if not relevant_refs:
            continue
        par_node = nodes.paragraph(classes=["glossary-refs"])
        par_node += nodes.strong(labels[type], labels[type])
        
        for ref in refs:
            if ref['type'] != type:
                continue
            ref_node = nodes.reference('', '')
            docnames = toc.get_toctree_ancestors(ref['docname'])
            if not docnames:
                docnames = [ref['docname']]
            for i, docname in enumerate(reversed(docnames)):
                if i < len(docnames) - 1:
                    for child in app.env.titles[docname].children:
                        ref_node.append(child)
                    ref_node.append(nodes.Text('/', '/'))
                else:
                    strong_node = nodes.strong('', '')
                    for child in app.env.titles[docname].children:
                        strong_node.append(child)
                    ref_node.append(strong_node)
            ref_node['refdocname'] = ref['docname']
            ref_node['refuri'] = app.builder.get_relative_uri(
                fromdocname, ref['docname'])
            ref_node['refuri'] += "#" + ref['target_id']
            par_node += ref_node
        par_nodes.append(par_node)
    return par_nodes

def process_glossary_list(app, doctree, fromdocname):
    env = app.builder.env
    if not hasattr(env, 'glossary_references'):
        env.glossary_references = {}

    for node in doctree.traverse(glossary_list):
        ## micha
        if not hasattr(node,"glossary_index"):
            return
        ## end micha
        index = node.glossary_index
        refs = env.glossary_references.get(index, [])
        node.replace_self(index_link_node(
            app, fromdocname, refs))

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
        env.note_dependency(_glossary_file_name(env.app))

        key, number, display = _parse_role_content(self.text)
        i = env.glossary_entries_index[key][number]
        entry = env.glossary_entries[i]


        target_id = 'gl-%s-%d' % (key, env.new_serialno('gl-' + key))
        target_node = nodes.target('', '', ids=[target_id])

        glossary_uri = env.app.config.glossary_doc
        if glossary_uri is not None:
            # avoids a presumed bug in the latex builder 
            if not isinstance(env.app.builder, LaTeXBuilder): 
                glossary_uri = env.app.builder.get_relative_uri(
                    env.docname, glossary_uri)
            glossary_uri += '#' + _def_target(key, number)

        node = glossary_reference(display, display,
            definition=entry['definition'],
            entry_name=entry['name'],
            uri=glossary_uri,
            number=entry['number'],
            classes=["glossary-ref"], **self.options)

        if not hasattr(env, 'glossary_references'):
            env.glossary_references = {}
        if not i in env.glossary_references:
            env.glossary_references[i] = []
        env.glossary_references[i].append({
            'type': 'USE',
            'docname': env.docname,
            'lineno': self.lineno,
            'target_id': target_id,
        })

        return [target_node, node], []

def setup(app):
    app.add_node(glossary_list,latex=(visit_glossary_list_latex,depart_glossary_list_latex))
    app.add_node(glossary_reference,
                 html=(visit_glossary_reference_html, depart_glossary_reference_html),
                 latex=(visit_glossary_reference_latex, depart_glossary_reference_latex))
 
    app.connect('env-before-read-docs', load_glossary_csv)
    app.connect('doctree-resolved', process_glossary_list)
    app.connect('env-purge-doc', purge_glossary_references)
    app.connect('env-merge-info', merge_glossary_references)
    app.add_directive('definition', GlossaryDefDirective)
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
