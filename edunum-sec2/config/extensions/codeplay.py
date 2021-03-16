
from base64 import b64encode

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective
from sphinx.util.osutil import relative_uri

class interactive_code(nodes.Element, nodes.General):
    pass

def visit_interactive_code_html(self, node):
    tag = self.starttag(node, "div", CLASS="interactive_code")
    self.body.append(tag.strip())

    prelude_attr = ""
    if len(node["prelude"]) > 0:
        prelude_attr = 'data-prelude="' + b64encode(node["prelude"].encode("UTF-8")).decode("UTF-8") + '" '
    afterword_attr = ""
    if len(node["afterword"]) > 0:
        afterword_attr = 'data-afterword="' + b64encode(node["afterword"].encode("UTF-8")).decode("UTF-8") + '" '
    hints_attr = ""
    if len(node["hints"]) > 0:
        string_hints = [hint for hint in node["hints"]]
        hints_attr = ('data-hints="' +
            ' '.join([b64encode(hint.encode("UTF-8")).decode("UTF-8") for hint in string_hints]) +
            '" ')


    self.body.append('<iframe src="' + node["codeplay_path"] + '" ' +
      prelude_attr + afterword_attr + hints_attr +
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
        "hints": directives.unchanged
    }
    has_content = True

    def run(self):
        self.assert_has_content()
        filename = self.env.doc2path(self.env.docname, base=None)
        codeplay, _ = self.env.relfn2path("/codeplay/frame.html")
        relative_path = relative_uri(filename, codeplay)

        def isSeparatorLine(line):
            line = line.strip()
            return len(line) >= 3 and line == "=" * len(line)

        pre = None
        post = None
        if "noprelude" not in self.options:
            i = 0
            while i < len(self.content):
                if isSeparatorLine(self.content[i]):
                    pre = i
                    i += 1
                    break
                i += 1
            while i < len(self.content):
                if isSeparatorLine(self.content[i]):
                    post = i
                    i += 1
                    break
                i += 1
        
        hints = []
        if "hints" in self.options:
            hint = []
            for line in self.options["hints"].splitlines():
                if isSeparatorLine(line) and len(hint) > 0:
                    hints.append('\n'.join(hint))
                    hint = []
                else:
                    hint.append(line)
            if len(hint) > 0:
                hints.append('\n'.join(hint))

        pre_lines = []
        post_lines = []
        code_lines = self.content
        
        if pre is not None:
            pre_lines = self.content[:pre]
            if post is not None:
                code_lines = self.content[pre + 1:post]
                post_lines = self.content[post + 1:]
            else:
                code_lines = self.content[pre + 1:]

        hints_node = nodes.paragraph()
        self.state.nested_parse(StringList(hints), 0, hints_node)

        container = interactive_code("",
          code='\n'.join(code_lines),
          prelude='\n'.join(pre_lines),
          hints=hints,
          hints_node=hints_node,
          afterword='\n'.join(post_lines),
          static="static" in self.options,
          nocontrols="nocontrols" in self.options,
          codeplay_path=relative_path,
          exec="exec" in self.options)
        self.set_source_info(container)

        return [container]

def setup(app):
    app.add_directive("codeplay", InteractiveCode)
    app.add_node(interactive_code, html=(visit_interactive_code_html, depart_interactive_code_html))
