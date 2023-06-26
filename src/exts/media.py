from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class LatexOnly(SphinxDirective):
    has_content = True

    def run(self):
        if self.env.app.builder.name != "latex":
            return []
        else:
            container = nodes.container()
            self.state.nested_parse(self.content, self.content_offset, container)
            return container.children

class HtmlOnly(SphinxDirective):
    has_content = True

    def run(self):
        if self.env.app.builder.name != "html":
            return []
        else:
            container = nodes.container()
            self.state.nested_parse(self.content, self.content_offset, container)
            return container.children

def setup(app):
    app.add_directive("latexonly", LatexOnly)
    app.add_directive("htmlonly", HtmlOnly)