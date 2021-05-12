
import os
import sys

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class youtube_video(nodes.Element, nodes.General):
    pass

def visit_youtube_html(self, node):
    extras = []
    if node["start"] is not None:
      extras.append(("start", str(node["start"])))
    if node["controls"] is not None and not node["controls"]:
      extras.append(("controls", "0"))

    extra = ""
    if len(extras) > 0:
      extra = "?" + '&'.join(key + "=" + value for (key, value) in extras)

    tag = self.starttag(node, "div", CLASS="youtube")
    self.body.append(tag.strip())
    self.body.append(
      '<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/' + 
      node["vid"] + extra + '" frameborder="0" ' +
      'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" ' + 
      'webkitallowfullscreen mozallowfullscreen allowfullscreen>"')

def depart_youtube_html(self, node):
    self.body.append("</iframe>")
    self.body.append("</div>")


class YouTubeVideo(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
      "start": directives.nonnegative_int,
      "nocontrols": directives.flag
    }
    has_content = False

    def run(self):
        video_id = self.arguments[0]
        container = youtube_video("",
          vid=video_id,
          start=self.options.get("start"),
          controls="nocontrols" not in self.options)
        self.set_source_info(container)

        return [container]

def setup(app):
    app.add_directive("youtube", YouTubeVideo)
    app.add_node(youtube_video, html=(visit_youtube_html, depart_youtube_html))

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    app.add_js_file("youtube.js")
    app.add_css_file("youtube.css")
