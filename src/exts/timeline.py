import os

from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives

class timeline_item(nodes.Element, nodes.General):
    pass

class timeline(nodes.Element, nodes.General):
    pass

def visit_timeline_html(self, node):
    self.body.append('''<div class="timeline">
            <div class="bar">
                <div></div>
            </div>
            <div class="items">
    ''')

def depart_timeline_html(self, node):
    self.body.append("</div></div>")

def visit_timeline_item_html(self, node):
    self.body.append(
        '<div class="item">' +
        '<div class="date">' +
        '<div>' + node['date'] + '</div>' +
        '</div>' +
        '<div class="content">' +
        ('<h2 class="item-title">' + node['title'] + '</h2>' if node['title'] is not None else ''))

def depart_timeline_item_html(self, node):
    self.body.append("</div></div>")

def visit_timeline_latex(self, node):
    self.body.append("\\begin{timeline} \n")
    
def depart_timeline_latex(self, node):
    self.body.append("\n \\end{timeline}")

def visit_timeline_item_latex(self, node):
    self.body.append("\\begin{timelineitem}{"
        +node['date']+ "}{" +  node['title']+"} \n")
    
def depart_timeline_item_latex(self, node):
    self.body.append("\n \\end{timelineitem}\n")

class TimelineItem(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        "title": directives.unchanged,
    }

    def run(self):
        node = timeline_item("", date=self.arguments[0], title=self.options.get('title', None))
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]

class Timeline(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}
    has_content = True

    def run(self):
        container = timeline("")
        self.set_source_info(container)
        self.state.nested_parse(self.content, self.content_offset, container)

        return [container]

def setup(app):
    app.add_directive("timeline", Timeline)
    app.add_directive("item", TimelineItem)
    app.add_node(timeline,
                 html=(visit_timeline_html, depart_timeline_html),
                 latex=(visit_timeline_latex, depart_timeline_latex))
    app.add_node(timeline_item,
                 html=(visit_timeline_item_html, depart_timeline_item_html),
                 latex=(visit_timeline_item_latex, depart_timeline_item_latex))

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    app.add_js_file("timeline.js")
    app.add_css_file("timeline.css")
