
function frameResized(self) {
  var frames = document.getElementsByClassName("codeframe")
  for (const frame of frames) {
    if (frame.contentWindow === self) {
      setTimeout(function() {
        frame.style.height = (self.document.body.scrollHeight + 30) + "px";
      }, 10);
    }
  }
}

function populateFrame(self, initialise) {
  var frames = document.getElementsByClassName("codeframe")
  for (const frame of frames) {
    if (frame.contentWindow === self) {
      initialise(frame);
    }
  }
}