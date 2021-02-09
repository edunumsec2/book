
from base64 import b64encode

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class interactive_code(nodes.Element, nodes.General):
    pass

def visit_interactive_code_html(self, node):
    tag = self.starttag(node, "div", CLASS="interactive_code")
    self.body.append(tag.strip())
    self.body.append('<iframe src="../../../skulpt/frame.html" ' + 
      'data-code="' + b64encode(node["code"].encode("UTF-8")).decode("UTF-8") +
      '" scrolling="no" ' + 
      ('data-run="true" ' if node["exec"] else '') +
      'class="codeframe" frameborder="0" border="0" cellspacing="0">')

def depart_interactive_code_html(self, node):
    self.body.append("</iframe>")
    self.body.append("</div>")


class InteractiveCode(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "exec": directives.flag
    }
    has_content = True

    def run(self):
        self.assert_has_content()

        container = interactive_code("",
          code='\n'.join(self.content),
          exec="exec" in self.options)
        self.set_source_info(container)

        return [container]

def setup(app):
    app.add_directive("codeplay", InteractiveCode)
    app.add_node(interactive_code, html=(visit_interactive_code_html, depart_interactive_code_html))
