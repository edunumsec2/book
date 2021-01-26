
import os
import sys

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class switchtube_video(nodes.Element, nodes.General):
    pass

def visit_switchtube_html(self, node):
    extras = []
    if node["title"] is not None and not node["title"]:
      extras.append(("title", "hide"))

    extra = ""
    if len(extras) > 0:
      extra = "?" + '&'.join(key + "=" + value for (key, value) in extras)

    tag = self.starttag(node, "div", CLASS="switchtube")
    self.body.append(tag.strip())
    self.body.append(
      '<iframe width="560" height="315" src="https://tube.switch.ch/embed/' + 
      node["vid"] + extra + '" frameborder="0" ' +
      'allow="fullscreen; encrypted-media; picture-in-picture" ' + 
      'allowfullscreen webkitallowfullscreen mozallowfullscreen>"')

def depart_switchtube_html(self, node):
    self.body.append("</iframe>")
    self.body.append("</div>")


class SwitchTubeVideo(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
      "notitle": directives.flag
    }
    has_content = False

    def run(self):
        video_id = self.arguments[0]
        container = switchtube_video("",
          vid=video_id,
          title="notitle" not in self.options)
        self.set_source_info(container)

        return [container]

def setup(app):
    app.add_directive("switchtube", SwitchTubeVideo)
    app.add_node(switchtube_video, html=(visit_switchtube_html, depart_switchtube_html))

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    app.add_js_file("switchtube.js")
    app.add_css_file("switchtube.css")
