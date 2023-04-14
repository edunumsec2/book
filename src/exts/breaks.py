from typing import List

from docutils import nodes  # type: ignore
from docutils.nodes import Node  # type: ignore
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxTranslator

# Page Break


class PageBreak(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = False

    def run(self) -> List[Node]:
        node = pagebreak()
        self.set_source_info(node)
        return [node]


class pagebreak(nodes.Element, nodes.General):
    pass


def pagebreak_latex(self: SphinxTranslator, node: Node) -> None:
    self.body.append("\n\\clearpage\n")


# Soft Page Break


class SoftPageBreak(SphinxDirective):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = False

    def run(self) -> List[Node]:
        node = softpagebreak()
        self.set_source_info(node)
        return [node]


class softpagebreak(nodes.Element, nodes.General):
    pass


def softpagebreak_latex(self: SphinxTranslator, node: Node) -> None:
    self.body.append(r"\n\pagebreak[4]\n")


def noop(self: SphinxTranslator, node: Node) -> None:
    pass


def setup(app: Sphinx) -> None:
    app.add_directive("pagebreak", PageBreak)
    app.add_node(
        pagebreak,
        html=(noop, noop),
        latex=(pagebreak_latex, noop),
    )
    app.add_directive("softpagebreak", SoftPageBreak)
    app.add_node(
        softpagebreak,
        html=(noop, noop),
        latex=(pagebreak_latex, noop),
    )
