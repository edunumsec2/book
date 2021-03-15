from base64 import b64encode

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.util.docutils import SphinxDirective
from sphinx.util.osutil import relative_uri

import urllib
import zlib


class logic_diagram(nodes.Element, nodes.General):
    pass


def begin_logic_diagram_html(self, node):

    content = node["content"].strip()
    height = node["height"]
    mode = node["mode"]
    showonly = node["showonly"]

    tag = self.starttag(
        node, "div", CLASS="logic_diagram", style="height: " + str(height) + "px;"
    )
    self.body.append(tag.strip())

    params = {}
    if mode and mode != "full":
        params["mode"] = mode
    if showonly:
        params["showonly"] = showonly
    if content:
        params["data"] = b64encode(content.encode("utf-8"), b"-_").decode("utf-8")

    param_str = urllib.parse.urlencode(params)

    self.body.append(
        '<iframe src="https://jp.pellet.name/hep/logiga?'
        + param_str
        + '" class="logicframe" frameborder="0" border="0" cellspacing="0">'
        + str(node)
    )


def end_logic_diagram_html(self, node):
    self.body.append("</iframe>")
    self.body.append("</div>")

def directive_mode(argument):
    return directives.choice(argument, ('static', 'tryout', 'connect', 'full'))

class LogicDiagram(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "height": directives.positive_int,
        "mode": directive_mode,
        "showonly": directives.unchanged,
    }
    has_content = True

    def run(self):
        self.assert_has_content()
        # filename = self.env.doc2path(self.env.docname, base=None)
        # codeplay, _ = self.env.relfn2path("/codeplay/frame.html")
        # relative_path = relative_uri(filename, codeplay)

        height = self.options.get("height", 500)
        mode = self.options.get("mode", "")
        showonly = self.options.get("showonly", "")

        node = logic_diagram(
            "",
            content="\n".join(self.content),
            height=height,
            mode=mode,
            showonly=showonly,
        )

        self.set_source_info(node)

        return [node]


def setup(app):
    app.add_directive("logic", LogicDiagram)
    app.add_node(logic_diagram, html=(begin_logic_diagram_html, end_logic_diagram_html))
