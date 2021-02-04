
function frameResized() {
  var frames = document.getElementsByClassName("codeframe")
  for (frame of frames) {
    frame.height = (frame.contentWindow.document.body.scrollHeight + 30) + "px";
  }
}