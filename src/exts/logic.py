from base64 import b64encode

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective, SphinxRole
from myst_parser.main import to_html

# import urllib
# import zlib
# import lzstring

class logic_diagram(nodes.Element, nodes.General):
    pass


def begin_logic_diagram_html(self, node):

    content = node["content"].strip()
    ref = node["ref"]
    height = node["height"]
    mode = node["mode"]
    showonly = node["showonly"]

    tag = self.starttag(
        node,
        "div",
        CLASS="logic-container",
        style="height: " + str(height) + "px;",
    )
    self.body.append(tag.strip())

    attrs_str = ""
    if ref:
        attrs_str += ' id="logic_' + ref + '"'
    if mode:
        attrs_str += ' mode="' + mode + '"'
    if showonly:
        attrs_str += ' showonly="' + showonly + '"'

    self.body.append(
        "<logic-editor"
        + attrs_str
        + ">"
        + "\n"
        + '<script type="application/json">'
        + "\n"
        + content
        + "\n"
    )


def end_logic_diagram_html(self, node):
    self.body.append("</script>")
    self.body.append("</logic-editor>")
    self.body.append("</div>")


def directive_mode(argument):
    return directives.choice(argument, ("static", "tryout", "connect", "full"))


class LogicDiagram(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "ref": directives.unchanged,
        "height": directives.positive_int,
        "mode": directive_mode,
        "showonly": directives.unchanged,
    }
    has_content = True

    def run(self):
        self.assert_has_content()

        ref = self.options.get("ref", "")
        height = self.options.get("height", 500)
        mode = self.options.get("mode", "")
        showonly = self.options.get("showonly", "")

        node = logic_diagram(
            "",
            content="\n".join(self.content),
            ref=ref,
            height=height,
            mode=mode,
            showonly=showonly,
        )

        self.set_source_info(node)

        return [node]


class logic_highlight(nodes.Inline, nodes.TextElement):
    pass



def _parse_highlight_content(string):
    def _parse_ids(string):
        if string.startswith("{") and string.endswith("}"):
            return string[1:-1].split(",")
        return [string]

    if '|' in string:
        [refs, display] = string.split('|', 2)
        if '.' in refs:
            [diagramrefs, componentrefs] = refs.split('.', 2)
            return _parse_ids(diagramrefs), _parse_ids(componentrefs), display

    return "", "", string


class LogicHighlightRefRole(SphinxRole):
    def run(self):
        diagramrefs, componentrefs, display = _parse_highlight_content(self.text)
        node = logic_highlight("", "",
            diagramrefs=diagramrefs,
            componentrefs=componentrefs,
            display=display,
            config=self.env.myst_config,
        )
        return [node], []


def _render_inline(source: str, config) -> str:
    # WARNING: this should not be called when creating the nodes
    # as it screws up the global parser state
    html = str(to_html(source, config=config)).strip()
    if html.startswith("<p>") and html.endswith("</p>"):
        html = html[3:-4]
    return html

def begin_logic_highlight_html(self, node):
    def _to_js_string(refs):
        if len(refs) == 1:
            return '"' + refs[0] + '"'
        return '[' + ', '.join(['"' + r + '"' for r in refs]) + ']'

    js_on_click = (
        'Logic.highlight(' + _to_js_string(node["diagramrefs"]) + ', ' + _to_js_string(node["componentrefs"]) + ')'
    )
    tag = self.starttag(
        node,
        "span",
        CLASS="logic-highlight",
        onclick=js_on_click,
    )
    self.body.append(tag.strip())
    content = _render_inline(node["display"], node["config"])
    self.body.append(content)



def end_logic_highlight_html(self, node):
    self.body.append("</span>")



class logic_gate(nodes.Inline, nodes.TextElement):
    pass

class LogicGateRole(SphinxRole):
    def run(self):
        node = logic_gate("", "",
            display=self.text,
        )
        return [node], []


def begin_logic_gate_html(self, node):
    tag = self.starttag(
        node,
        "span",
        CLASS="logic-gate",
    )
    self.body.append(tag.strip())
    self.body.append(node["display"])

def end_logic_gate_html(self, node):
    self.body.append("</span>")


def setup(app):
    app.add_directive("logic", LogicDiagram)
    app.add_node(logic_diagram, html=(begin_logic_diagram_html, end_logic_diagram_html))
    app.add_js_file("https://logic.modulo-info.ch/simulator/lib/bundle.js")

    app.add_role("logicref", LogicHighlightRefRole())
    app.add_node(
        logic_highlight, html=(begin_logic_highlight_html, end_logic_highlight_html)
    )

    app.add_role("lg", LogicGateRole())
    app.add_node(
        logic_gate, html=(begin_logic_gate_html, end_logic_gate_html)
    )


    app.add_css_file("logic.css")
