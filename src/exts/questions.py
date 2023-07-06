
import os
import sys

from docutils import nodes
from docutils.nodes import Node  # type: ignore
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class answer(nodes.TextElement, nodes.Inline):
    is_correct = None

class correct_answer(answer):
    is_correct = True

class incorrect_answer(answer):
    is_correct = False

class question(nodes.admonition):
    correct = []
    counter = 0
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("question")

class check_buttons(nodes.Element, nodes.General):
    pass

def visit_answer_html(self, node):
    classes = ["answer"]
    if node.is_correct:
        classes.append("correct")
    else:
        classes.append("incorrect")

    tag = self.starttag(node, "label", CLASS=" ".join(classes))
    self.body.append(tag.strip())
    self.body.append("<input type=\"checkbox\" />")
    

def depart_answer_html(self, node):
    self.body.append("</label>")

def visit_question_html(self, node):
    self.visit_admonition(node)
    classes = ["question"]
    if node["multi"]:
        classes.append("multi")

    tag = self.starttag(node, "div", CLASS=" ".join(classes))
    self.body.append(tag.strip())
    self.body.append("<form>")

def depart_question_html(self, node):
    self.body.append("</form>")
    self.body.append("</div>")
    self.depart_admonition(node)

def visit_check_buttons_html(self, node):
    tag = self.starttag(node, "div", CLASS="controls")
    self.body.append(tag.strip())
    self.body.append("<button type=\"button\" class=\"reset btn btn-secondary\"><i class=\"fa fa-repeat\"></i> Effacer</button>")
    self.body.append("<button type=\"button\" class=\"show btn btn-secondary\"><i class=\"fa fa-eye\"></i> Montrer</button>")
    self.body.append("<button type=\"button\" class=\"check btn btn-primary\"><i class=\"fa fa-question\"></i> Vérifier</button>")

def depart_check_buttons_html(self, node):
    self.body.append("</div>")

### latex (by Micha) 
def visit_answer_latex(self, node):
    classes = ["answer"]
    if node.is_correct:
        classes.append("correct")
        question.correct.append(question.counter)
    else:
        classes.append("incorrect")
    question.counter += 1
    


def depart_answer_latex(self, node):
    pass


def visit_question_latex(self, node: Node):
    classes = ["question"]
    if node["multi"]:
        classes.append("multi")
    question.correct = []
    question.counter = 0
   
    self.body.append('\n\\begin{question}')

    def convert_itemize(node: Node):
        """Recursively convert all bullet lists to enumerated lists.
        We want this because we refer to answers by number."""
        if isinstance(node, nodes.bullet_list):
            node.__class__ = nodes.enumerated_list
        else:
            for child in node.children:
                convert_itemize(child)

    convert_itemize(node)

    


    
def depart_question_latex(self, node):
     self.body.append('\n\\end{question}\n')
   
def visit_check_buttons_latex(self, node):
    responses = [str(i+1) for i in question.correct]
    self.body.append(r"\insertsolution{"+ ",".join(responses)+"}\n")

def depart_check_buttons_latex(self, node):
    pass



class Question(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "multi": directives.flag
    }
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = question("", multi="multi" in self.options)
        

        title = self.arguments[0] if len(self.arguments) > 0 else "Question"
        #title ="Question"
        #if len(self.arguments) > 0: 
        #    title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        def isSeparatorLine(line):
            line = line.strip()
            return len(line) >= 3 and line == "=" * len(line)
        
        feedback_start = None
        for i, line in enumerate(self.content):
            if isSeparatorLine(line):
                feedback_start = i
                break
        
        question_content = self.content

        feedback_content = None
        if feedback_start is not None:
            question_content = self.content[:feedback_start]
            feedback_content = self.content[feedback_start+1:]

        content = nodes.container("", is_div=True, classes=["question-content"])
        self.state.nested_parse(question_content, self.content_offset, content)
        admonition += content

        buttons = check_buttons("")
        admonition += buttons

        if feedback_content is not None:
            feedback = nodes.container("", is_div=True, classes=["question-feedback"])
            self.state.nested_parse(feedback_content, self.content_offset, feedback)
            admonition += feedback
    
        return [admonition]
    
## todo: update Micha
def setup(app):
    app.add_directive("question", Question)
    app.add_node(question,
                 html=(visit_question_html, depart_question_html),
                 latex=(visit_question_latex, depart_question_latex))
    app.add_node(correct_answer,
                 html=(visit_answer_html, depart_answer_html),
                 latex=(visit_answer_latex, depart_answer_latex))
    app.add_node(incorrect_answer,
                 html=(visit_answer_html, depart_answer_html),
                 latex=(visit_answer_latex, depart_answer_latex))
    app.add_node(check_buttons,
                 html=(visit_check_buttons_html, depart_check_buttons_html),
                 latex=(visit_check_buttons_latex, depart_check_buttons_latex))
    app.add_generic_role("v", correct_answer)
    app.add_generic_role("f", incorrect_answer)

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    app.add_js_file("questions.js")
    app.add_css_file("questions.css")
