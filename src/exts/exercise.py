from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class Exercise(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title = self.arguments[0] if len(self.arguments) > 0 else "Exercice"

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["question-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

def setup(app):
    app.add_directive("exercise", Exercise)

    # static_dir = os.path.join(os.path.dirname(__file__), "static")
    # app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    # app.add_js_file("exercise.js")
    # app.add_css_file("exercise.css")
