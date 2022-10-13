from docutils import nodes
from sphinx.util.docutils import SphinxDirective
from docutils.parsers.rst import directives

class gallery(nodes.Element, nodes.General):
    pass

class gallery_image(nodes.Element, nodes.General):
    pass

def visit_gallery_html(self, node):
    tag = self.starttag(node, "div", CLASS="gallery")
    self.body.append(tag.strip())

def depart_gallery_html(self, node):
    self.body.append("</div>")

def visit_gallery_image_html(self, node):
    tag = self.starttag(node, "div", CLASS="gallery-element")
    self.body.append(tag.strip())

def depart_gallery_image_html(self, node):
    self.body.append("</div>")

class GalleryDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        node = gallery()
        self.state.nested_parse(self.content, self.content_offset, node)

        # Wrap each node in a gallery_image node
        for i, child in enumerate(node.children):
            new_node = gallery_image()
            new_node.children = [child]
            node.children[i] = new_node

        return [node]

class GalleryImageDirective(directives.images.Image):

    option_spec = directives.images.Image.option_spec.copy()
    option_spec.update({
        'url': directives.uri,
    })

    def run(self):
        node = super(GalleryImageDirective, self).run()[0]
        node["classes"].append("gallery-image")
        if "url" in self.options:
            new_node = nodes.reference("", "", internal=False, refuri=self.options["url"])
            new_node["classes"].append("gallery-link")
            new_node.children = [node]
            node.parent = new_node
            node = new_node
        return [node]

def setup(app):
    app.add_node(gallery, html=(visit_gallery_html, depart_gallery_html))
    app.add_node(gallery_image, html=(visit_gallery_image_html, depart_gallery_image_html))
    app.add_directive("gallery", GalleryDirective)
    app.add_directive("picture", GalleryImageDirective)
