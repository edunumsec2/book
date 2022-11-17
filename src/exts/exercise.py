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


class ToGoFurther(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="Pour aller plus loin"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["togofurther-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class MicroActivity(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="Micro-activité"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["micro-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class Important(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="Important"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["important-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class DidYouKnow(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="Le saviez-vous ?"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["didyouknow-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class Reminder(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="Rappel"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["reminder-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class Related(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="En lien"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["related-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class Eval(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="Ai-je compris ?"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["eval-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class ThinkingMatter(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="Matière à réfléchir"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["thinkingmatter-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class Note(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="Remarque"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["note-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class ToRecall(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="À retenir"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["torecall-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

class Document(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        self.assert_has_content()

        admonition = nodes.admonition("")

        title ="Document"
        if len(self.arguments) > 0: 
            title += ": " + self.arguments[0]

        textnodes, _ = self.state.inline_text(title, self.lineno)
        label = nodes.title(title, *textnodes)
        admonition += label

        content = nodes.container("", is_div=True, classes=["document-content"])
        self.state.nested_parse(self.content, self.content_offset, content)
        admonition += content

        return [admonition]

def setup(app):
    app.add_directive("exercise", Exercise)
    app.add_directive("togofurther", ToGoFurther)
    app.add_directive("micro", MicroActivity)
    app.add_directive("important", Important)
    app.add_directive("didyouknow", DidYouKnow)
    app.add_directive("reminder", Reminder)
    app.add_directive("related", Related)
    app.add_directive("eval", Eval)
    app.add_directive("thinkingmatter", ThinkingMatter)
    app.add_directive("note", Note)
    app.add_directive("torecall", ToRecall)
    app.add_directive("document", Document)




    # static_dir = os.path.join(os.path.dirname(__file__), "static")
    # app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    # app.add_js_file("exercise.js")
    # app.add_css_file("exercise.css")
