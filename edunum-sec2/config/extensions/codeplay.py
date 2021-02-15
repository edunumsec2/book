
from base64 import b64encode

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class interactive_code(nodes.Element, nodes.General):
    pass

def visit_interactive_code_html(self, node):
    tag = self.starttag(node, "div", CLASS="interactive_code")
    self.body.append(tag.strip())

    prelude_attr = ""
    if len(node["prelude"]) > 0:
        prelude_attr = 'data-prelude="' + b64encode(node["prelude"].encode("UTF-8")).decode("UTF-8") + '" '

    self.body.append('<iframe src="/codeplay/frame.html" ' +
      prelude_attr +
      'data-code="' + b64encode(node["code"].encode("UTF-8")).decode("UTF-8") + '" ' +
      'scrolling="no" ' + 
      ('data-run="true" ' if node["exec"] else '') +
      ('data-static="true" ' if node["static"] else '') +
      ('data-nocontrols="true" ' if node["nocontrols"] else '') +
      'class="codeframe" frameborder="0" border="0" cellspacing="0">')

def depart_interactive_code_html(self, node):
    self.body.append("</iframe>")
    self.body.append("</div>")


class InteractiveCode(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "exec": directives.flag,
        "noprelude": directives.flag,
        "static": directives.flag,
        "nocontrols": directives.flag,
    }
    has_content = True

    def run(self):
        self.assert_has_content()

        pre = None
        if "noprelude" not in self.options:
            i = 0
            while i < len(self.content):
                if self.content[i].strip() == "=" * 3:
                    pre = i
                    break
                i += 1
        
        pre_lines = []
        code_lines = self.content
        
        if pre is not None:
            pre_lines = self.content[:pre]
            code_lines = self.content[pre + 1:]

        container = interactive_code("",
          code='\n'.join(code_lines),
          prelude='\n'.join(pre_lines),
          static="static" in self.options,
          nocontrols="nocontrols" in self.options,
          exec="exec" in self.options)
        self.set_source_info(container)

        return [container]

def setup(app):
    app.add_directive("codeplay", InteractiveCode)
    app.add_node(interactive_code, html=(visit_interactive_code_html, depart_interactive_code_html))
