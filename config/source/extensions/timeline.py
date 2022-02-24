from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class timeline(nodes.Element, nodes.General):
    pass

def visit_timeline_html(self, node):
    self.body.append(
        '<iframe src="https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=' +
        node["tid"] + '&font=Default&lang=fr&initial_zoom=2&height=650" width="800" height="650"' +
        'webkitallowfullscreen mozallowfullscreen allowfullscreen frameborder="0">')

def depart_timeline_html(self, node):
    self.body.append("</iframe>")

class Timeline(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}
    has_content = False

    def run(self):
        timeline_id = self.arguments[0]
        container = timeline("", tid=timeline_id)
        self.set_source_info(container)

        return [container]

def setup(app):
    app.add_directive("timeline", Timeline)
    app.add_node(timeline, html=(visit_timeline_html, depart_timeline_html))