
import os
import sys
import qrcode

from PIL import Image

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

class youtube_video(nodes.Element, nodes.General):
    counter = 0

def get_extra(node):
    extras = []
    if node["start"] is not None:
      extras.append(("start", str(node["start"])))
    if node["controls"] is not None and not node["controls"]:
      extras.append(("controls", "0"))

    extra = ""
    if len(extras) > 0:
      extra = "?" + '&'.join(key + "=" + value for (key, value) in extras)
    return extra

def visit_youtube_html(self, node):
    # extras = []
    # if node["start"] is not None:
    #   extras.append(("start", str(node["start"])))
    # if node["controls"] is not None and not node["controls"]:
    #   extras.append(("controls", "0"))
    # extra = ""
    # if len(extras) > 0:
    #   extra = "?" + '&'.join(key + "=" + value for (key, value) in extras)

    extra = get_extra(node)
    
    tag = self.starttag(node, "div", CLASS="video")
    self.body.append(tag.strip())
    self.body.append(
      '<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/' + 
      node["vid"] + extra + '" frameborder="0" ' +
      'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" ' + 
      'webkitallowfullscreen mozallowfullscreen allowfullscreen>"')

def depart_youtube_html(self, node):
    self.body.append("</iframe>")
    self.body.append("</div>")

# micha
def visit_youtube_latex(self, node):
    extra = get_extra(node)
    src='https://www.youtube-nocookie.com/embed/' + node["vid"] + extra
    qrcode_folder = os.path.join(self.builder.outdir, "video_png")
    if not os.path.exists(qrcode_folder):
        os.makedirs(qrcode_folder)
    youtube_video.counter += 1
    qrfilename = os.path.join(qrcode_folder, f"qr{youtube_video.counter}.png")
    qr = qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(src)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(qrfilename)                              

    #self.body.append("Vidéo youtube "+str(youtube_video.counter) + ": " + src + "\\\ \n")
    self.body.append(f"\n\insertvideo{{{qrfilename}}}{{{src}}}{{{youtube_video.counter}}}\n")
   
                              
def depart_youtube_latex(self, node):
    pass

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

class switchtube_video(nodes.Element, nodes.General):
    pass

def visit_switchtube_html(self, node):
    extras = []
    if node["title"] is not None and not node["title"]:
      extras.append(("title", "hide"))

    extra = ""
    if len(extras) > 0:
      extra = "?" + '&'.join(key + "=" + value for (key, value) in extras)

    start = ""
    if node["start"] is not None:
      seconds = node["start"] % 60
      minutes = node["start"] // 60
      start = "#" + str(minutes) + ":" + str(seconds)

    tag = self.starttag(node, "div", CLASS="video")
    self.body.append(tag.strip())
    self.body.append(
      '<iframe width="560" height="315" src="https://tube.switch.ch/embed/' + 
      node["vid"] + start + extra + '" frameborder="0" ' +
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
      "start": directives.nonnegative_int,
      "notitle": directives.flag
    }
    has_content = False

    def run(self):
        video_id = self.arguments[0]
        container = switchtube_video("",
          vid=video_id,
          start=self.options.get("start"),
          title="notitle" not in self.options)
        self.set_source_info(container)

        return [container]

class cnrs_video(nodes.Element, nodes.General):
    pass

def visit_cnrs_html(self, node):
    tag = self.starttag(node, "div", CLASS="video")
    self.body.append(tag.strip())
    self.body.append('<div class="cnrs">')
    self.body.append(
      '<iframe width="800" height="450" src="https://mediavideo.cnrs.fr/player_export.php?code=' + 
      node["vid"] + '" frameborder="0" ' +
      'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" ' + 
      'webkitallowfullscreen mozallowfullscreen allowfullscreen>"')

def depart_cnrs_html(self, node):
    self.body.append("</iframe>")
    self.body.append("</div>")
    self.body.append("</div>")

class CNRSVideo(SphinxDirective):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}
    has_content = False

    def run(self):
        video_id = self.arguments[0]
        container = cnrs_video("", vid=video_id)
        self.set_source_info(container)

        return [container]

def setup(app):
    app.add_directive("youtube", YouTubeVideo)
    app.add_directive("switchtube", SwitchTubeVideo)
    app.add_directive("cnrs", CNRSVideo)
    
    app.add_node(youtube_video,
                 html=(visit_youtube_html, depart_youtube_html),
                 latex=(visit_youtube_latex, depart_youtube_latex))
    app.add_node(switchtube_video, html=(visit_switchtube_html, depart_switchtube_html))
    app.add_node(cnrs_video, html=(visit_cnrs_html, depart_cnrs_html))

    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.connect("builder-inited", (lambda app: app.config.html_static_path.append(static_dir)))
    app.add_css_file("videos.css")
