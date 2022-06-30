
from base64 import b64encode

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective
from sphinx.util.osutil import relative_uri, canon_path

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
      'data-file="' + b64encode(node["file"].encode("UTF-8")).decode("UTF-8") + '" ' +
      ('data-output-min-lines="' + str(node["min_height"]) + '" ' if node["min_height"] is not None else "") +
      ('data-output-max-lines="' + str(node["max_height"]) + '" ' if node["max_height"] is not None else "") +
      'scrolling="no" ' + 
      ('data-run="true" ' if node["exec"] else '') +
      ('data-static="true" ' if node["static"] else '') +
      ('data-nocontrols="true" ' if node["nocontrols"] else '') +
      ('data-download-hide-prelude="true" ' if node["hide_prelude_in_download"] else '') +
      ('data-download-hide-afterword="true" ' if node["hide_afterword_in_download"] else '') +
      'class="codeframe" frameborder="0" border="0" cellspacing="0">')

def depart_interactive_code_html(self, node):
    self.body.append("</iframe>")
    self.body.append("</div>")

def visit_interactive_code_latex(self, node):
    self.body.append("\\begin{lstlisting}\n")
    self.body.append(node["code"].strip())

def depart_interactive_code_latex(self, node):
    self.body.append("\n \\end{lstlisting}")
    
class InteractiveCode(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "exec": directives.flag,
        "noprelude": directives.flag,
        "static": directives.flag,
        "nocontrols": directives.flag,
        "hints": directives.unchanged,
        "file": directives.unchanged,
        "output_lines": directives.nonnegative_int,
        "min_output_lines": directives.nonnegative_int,
        "max_output_lines": directives.nonnegative_int,
        "hide_prelude_in_download": directives.flag,
        "hide_afterword_in_download": directives.flag,
    }
    has_content = True

    

        
    def run(self):
        self.assert_has_content()
        filename = canon_path(self.env.doc2path(self.env.docname, base=None))
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

        min_height = None
        max_height = None
        if "output_lines" in self.options:
            min_height = self.options["output_lines"]
            max_height = self.options["output_lines"]
        if "min_output_lines" in self.options:
            min_height = self.options["min_output_lines"]
        if "max_output_lines" in self.options:
            max_height = self.options["max_output_lines"]
        if min_height is not None and max_height is not None and min_height > max_height:
            raise ValueError("Min output line count cannot be greater than max.")

        container = interactive_code("",
          code='\n'.join(code_lines),
          prelude='\n'.join(pre_lines),
          hints=hints,
          hints_node=hints_node,
          afterword='\n'.join(post_lines),
          static="static" in self.options,
          nocontrols="nocontrols" in self.options,
          codeplay_path=relative_path,
          exec="exec" in self.options,
          file=self.options["file"] if "file" in self.options else "code.py",
          min_height=min_height,
          max_height=max_height,
          hide_prelude_in_download="hide_prelude_in_download" in self.options,
          hide_afterword_in_download="hide_afterword_in_download" in self.options)
        self.set_source_info(container)

        return [container]

def setup(app):
    app.add_directive("codeplay", InteractiveCode)
    app.add_node(interactive_code,
                 html=(visit_interactive_code_html, depart_interactive_code_html),
                 latex=(visit_interactive_code_latex, depart_interactive_code_latex))
    app.add_css_file("codeplay.css")
