
import os
import sys

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class answer(nodes.TextElement, nodes.Inline):
    is_correct = None

class correct_answer(answer):
    is_correct = True

class incorrect_answer(answer):
    is_correct = False

class question(nodes.Element, nodes.General):
    pass

class check_buttons(nodes.Element, nodes.General):
    pass

def visit_answer_html(self, node):
    attributes = node.attributes.copy()
    attributes.pop("backrefs")
    attributes.pop("classes")
    attributes.pop("dupnames")
    attributes.pop("ids")
    attributes.pop("names")

    classes = ["answer"]
    if node.is_correct:
        classes.append("correct")
    else:
        classes.append("incorrect")

    tag = self.starttag(node, "span", CLASS=" ".join(classes), **attributes)
    self.body.append(tag.strip())
    self.body.append("<input type=\"checkbox\" />")

def depart_answer_html(self, node):
    self.body.append("</span>")

def visit_question_html(self, node):
    attributes = node.attributes.copy()
    attributes.pop("backrefs")
    attributes.pop("classes")
    attributes.pop("dupnames")
    attributes.pop("ids")
    attributes.pop("names")

    tag = self.starttag(node, "div", CLASS="question", **attributes)
    self.body.append(tag.strip())
    self.body.append("<form>")

def depart_question_html(self, node):
    self.body.append("</form>")
    self.body.append("</div>")

def visit_check_buttons_html(self, node):
    self.body.append("<input type=\"button\" class=\"check\" value=\"Vérifier ma réponse\" />")

def depart_check_buttons_html(self, node):
    pass


class Question(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {}
    has_content = True

    def run(self):
        self.assert_has_content()

        container = question("")
        self.set_source_info(container)

        admonition = nodes.admonition("")

        title = self.arguments[0] if len(self.arguments) > 0 else "Question"

        textnodes, messages = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)

        content = nodes.container("", is_div=True, classes=["question-content"])
        self.state.nested_parse(self.content, self.content_offset, content)

        buttons = check_buttons("")

        admonition += label
        admonition += content
        admonition += buttons

        container += admonition

        return [container]

def setup(app):
    app.add_directive("question", Question)
    app.add_node(question, html=(visit_question_html, depart_question_html))
    app.add_node(correct_answer, html=(visit_answer_html, depart_answer_html))
    app.add_node(incorrect_answer, html=(visit_answer_html, depart_answer_html))
    app.add_node(check_buttons, html=(visit_check_buttons_html, depart_check_buttons_html))
    app.add_generic_role("v", correct_answer)
    app.add_generic_role("f", incorrect_answer)

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    app.add_js_file("questions.js")
    app.add_css_file("questions.css")
