
import os

from docutils import nodes

class blank(nodes.General, nodes.Element, nodes.Inline):
    pass

class blank_option(nodes.TextElement, nodes.Inline):
    pass

def visit_blank_html(self, node):
    tag = self.starttag(node, "select", CLASS="blank")
    self.body.append(tag.strip())
    self.body.append("<option class=\"blank_option\" value=\"-1\" selected=\"selected\"></option>")

def depart_blank_html(self, node):
    self.body.append("</select>")

def visit_option_html(self, node):
    CLASS = "correct_option" if node["correct"] else "incorrect_option"
    value = "1" if node["correct"] else "0"
    tag = self.starttag(node, "option", value=value, CLASS=CLASS)
    self.body.append(tag.strip())
    self.body.append(node["value"])

def depart_option_html(self, node):
    self.body.append("</option>")

def visit_blank_latex(self, node): # not implemented
    pass

def depart_blank_latex(self, node): # not implemented
    pass

def visit_option_latex(self, node): # not implemented
    pass

def depart_option_latex(self, node): # not implemented
    pass

def blank_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = blank("")
    answers = text.split('|')
    for answer in answers:
        correct = False
        lead = answer[0]
        if lead == '>':
            answer = answer[1:]
            correct = True
        node += blank_option(value=answer, correct=correct)
    return [node], []

def setup(app):
    app.add_node(blank, html=(visit_blank_html, depart_blank_html),
                 latex=(visit_blank_latex, depart_blank_latex))
    app.add_node(blank_option, html=(visit_option_html, depart_option_html),
                 latex=(visit_option_latex, depart_option_latex))
    blank_role.content = True
    blank_role.options = {}
    app.add_role("bl", blank_role)

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    app.add_js_file("blanks.js")
    app.add_css_file("blanks.css")
