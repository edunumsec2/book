
from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class only_role(nodes.Element, nodes.General):
    pass

def visit_only_role_html(self, node):
    pass

def depart_only_role_html(self, node):
    pass

class OnlyRole(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}
    has_content = True

    def run(self):
        self.assert_has_content()
        content = only_role("")
        role = self.arguments[0].strip()
        if role == self.config.user_role:
            self.state.nested_parse(self.content, self.content_offset, content)

        return [content]

def setup(app):
    app.add_config_value("user_role", None, "env")
    app.add_directive("role", OnlyRole)
    app.add_node(only_role, html=(visit_only_role_html, depart_only_role_html))

