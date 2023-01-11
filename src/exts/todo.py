from docutils import nodes
from sphinx.util.docutils import SphinxDirective, SphinxRole
import sphinx.ext.todo
#from sphinx.util.nodes import nested_parse_with_titles
#from sphinx.builders.latex import LaTeXBuilder
import os.path

class TodoNode(nodes.Inline,nodes.TextElement):
    pass

def do_nothing(self, node):
    pass

def visit_todo_node_html(self,node):
    self.body.append('<span class="todo">')

def depart_todo_node_html(self,node):
    self.body.append('</span>')


class TodoRole(SphinxRole):
    def run(self):
        if hasattr(self.env.app.config,'todo_include_todos'):
            if self.env.app.config.todo_include_todos:
                node = TodoNode(self.text,self.text)
                return [node],[]
        return [],[]    

def setup(app):
    app.add_node(TodoNode, html=(visit_todo_node_html, depart_todo_node_html))
    app.add_role('itodo', TodoRole())
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    app.add_css_file("todo.css")