from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from sphinx.writers.html import HTMLTranslator


class exercise(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("exercise")

def visit_exercise_latex(self, node):
    self.body.append('\n\\begin{exercise}')

def depart_exercise_latex(self, node):
    self.body.append('\n\\end{exercise}\n')

class Exercise(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        "num": directives.nonnegative_int,
    }

    nextNumberByDoc = {}

    def run(self):
        self.assert_has_content()

        # admonition = nodes.admonition("", classes=["admonition", "note"])
        admonition = exercise()
        admonition.set_class("note")

        label = self.arguments[0] if len(self.arguments) > 0 else None

        if "num" in self.options:
            Exercise.nextNumberByDoc[self.env.docname] = self.options["num"]
        elif self.env.docname not in Exercise.nextNumberByDoc:
            Exercise.nextNumberByDoc[self.env.docname] = 1

        number = Exercise.nextNumberByDoc[self.env.docname]
        Solution.lastQuestion[self.env.docname] = (number, label)
        Exercise.nextNumberByDoc[self.env.docname] += 1

        title = "Exercice {}".format(number)
        if label is not None:
            title += " – {}".format(label)

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["question-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]



class solution(nodes.admonition, nodes.hint):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("solution")

def visit_solution_latex(self, node):
    self.body.append('\n\\begin{solution}')

def depart_solution_latex(self, node):
    self.body.append('\n\\end{solution}\n')


class Solution(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    lastQuestion = {}

    def run(self):
        self.assert_has_content()

        #admonition = nodes.admonition("", classes=["admonition", "hint"])
        admonition = solution()
        admonition.set_class("hint")

        title = "Solution"
        last_question = Solution.lastQuestion.get(self.env.docname, None)
        if last_question is not None:
            del Solution.lastQuestion[self.env.docname]
            number, label = last_question
            title += " {}".format(number)
            if label is not None:
                title += " – {}".format(label)

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["solution-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class to_go_further(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("togofurther")

def visit_to_go_further_latex(self, node):
    self.body.append('\n\\begin{togofurther}')

def depart_to_go_further_latex(self, node):
    self.body.append('\n\\end{togofurther}\n')

class ToGoFurther(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = to_go_further("")

        title ="Pour aller plus loin"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["togofurther-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class micro_activity(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("microactivity")

def visit_micro_activity_latex(self, node):
    self.body.append('\n\\begin{microactivity}')

def depart_micro_activity_latex(self, node):
    self.body.append('\n\\end{microactivity}\n')

class MicroActivity(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = micro_activity("")

        title ="Micro-activité"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["micro-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class important(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("important")

def visit_important_latex(self, node):
    self.body.append('\n\\begin{important}')

def depart_important_latex(self, node):
    self.body.append('\n\\end{important}\n')

class Important(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = important("")

        title ="Important"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["important-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class did_you_know(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("didyouknow")

def visit_did_you_know_latex(self, node):
    self.body.append('\n\\begin{didyouknow}')

def depart_did_you_know_latex(self, node):
    self.body.append('\n\\end{didyouknow}\n')

class DidYouKnow(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = did_you_know("")

        title ="Le saviez-vous ?"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["didyouknow-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class reminder(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("reminder")

def visit_reminder_latex(self, node):
    self.body.append('\n\\begin{reminder}')

def depart_reminder_latex(self, node):
    self.body.append('\n\\end{reminder}\n')

class Reminder(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = reminder("")

        title ="Rappel"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["reminder-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]


class related(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("related")

def visit_related_latex(self, node):
    self.body.append('\n\\begin{related}')

def depart_related_latex(self, node):
    self.body.append('\n\\end{related}\n')

class Related(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = related("")

        title ="En lien"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["related-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class evaluation(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("evaluation")

def visit_eval_latex(self, node):
    self.body.append('\n\\begin{evaluation}')

def depart_eval_latex(self, node):
    self.body.append('\n\\end{evaluation}\n')

class Eval(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = evaluation("")

        title ="Ai-je compris ?"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["eval-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]


class thinking_matter(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("thinkingmatter")

def visit_thinking_matter_latex(self, node):
    self.body.append('\n\\begin{thinkingmatter}')

def depart_thinking_matter_latex(self, node):
    self.body.append('\n\\end{thinkingmatter}\n')

class ThinkingMatter(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = thinking_matter("")

        title ="Matière à réfléchir"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["thinkingmatter-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]


class note(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("note")

def visit_note_latex(self, node):
    self.body.append('\n\\begin{note}')

def depart_note_latex(self, node):
    self.body.append('\n\\end{note}\n')

class Note(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = note("")

        title ="Remarque"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["note-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class to_recall(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("torecall")

def visit_to_recall_latex(self, node):
    self.body.append('\n\\begin{torecall}')

def depart_to_recall_latex(self, node):
    self.body.append('\n\\end{torecall}\n')
    
class ToRecall(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = to_recall("")

        title ="À retenir"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["torecall-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]


class historic_document(nodes.admonition):
    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self["classes"].append("historicdocument")

def visit_document_latex(self, node):
    self.body.append('\n\\begin{historicdocument}')

def depart_document_latex(self, node):
    self.body.append('\n\\end{historicdocument}\n')
class HistoricDocument(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = historic_document("")

        title ="Document historique"
        if len(self.arguments) > 0: 
            title += " – " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["document-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

def visit_admonition_html(self, node):
    self.visit_admonition(node)

def depart_admonition_html(self, node):
    self.depart_admonition(node)





def setup(app):
    app.add_directive("exercise", Exercise)
    app.add_directive("solution", Solution)
    app.add_directive("togofurther", ToGoFurther)
    app.add_directive("micro", MicroActivity)
    app.add_directive("important", Important, override=True)
    app.add_directive("didyouknow", DidYouKnow)
    app.add_directive("reminder", Reminder)
    app.add_directive("related", Related)
    app.add_directive("eval", Eval)
    app.add_directive("thinkingmatter", ThinkingMatter)
    app.add_directive("note", Note, override=True)
    app.add_directive("torecall", ToRecall)
    app.add_directive("document", HistoricDocument)


    # good for latex compilation but not for html...

  
    app.add_node(micro_activity, latex=(visit_micro_activity_latex, depart_micro_activity_latex),
                                html=(visit_admonition_html, depart_admonition_html))
    app.add_node(to_go_further,latex=(visit_to_go_further_latex,depart_to_go_further_latex),
                                html=(visit_admonition_html, depart_admonition_html))
    app.add_node(important,latex=(visit_important_latex,depart_important_latex),
                                html=(visit_admonition_html, depart_admonition_html), override=True)
    app.add_node(did_you_know,latex=(visit_did_you_know_latex,depart_did_you_know_latex),
                                html=(visit_admonition_html, depart_admonition_html))
    app.add_node(reminder,latex=(visit_reminder_latex,depart_reminder_latex),
                                html=(visit_admonition_html, depart_admonition_html))
    app.add_node(related,latex=(visit_related_latex,depart_related_latex),
                                html=(visit_admonition_html, depart_admonition_html))
    app.add_node(evaluation,latex=(visit_eval_latex,depart_eval_latex),
                                html=(visit_admonition_html, depart_admonition_html))
    app.add_node(thinking_matter,latex=(visit_thinking_matter_latex,depart_thinking_matter_latex),
                                html=(visit_admonition_html, depart_admonition_html))
    app.add_node(note,latex=(visit_note_latex,depart_note_latex),
                                html=(visit_admonition_html, depart_admonition_html), override=True)
    app.add_node(to_recall,latex=(visit_to_recall_latex,depart_to_recall_latex),
                                html=(visit_admonition_html, depart_admonition_html))
    app.add_node(historic_document,latex=(visit_document_latex,depart_document_latex),
                                html=(visit_admonition_html, depart_admonition_html))
    app.add_node(exercise, latex=(visit_exercise_latex, depart_exercise_latex),
                                html=(visit_admonition_html, depart_admonition_html))  
    app.add_node(solution, latex=(visit_solution_latex, depart_solution_latex),
                                html=(visit_admonition_html, depart_admonition_html))  

    # static_dir = os.path.join(os.path.dirname(__file__), "static")
    # app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    # app.add_js_file("exercise.js")
    # app.add_css_file("exercise.css")
