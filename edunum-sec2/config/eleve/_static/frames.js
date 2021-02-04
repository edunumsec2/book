
function frameResized() {
  var frames = document.getElementsByClassName("codeframe")
  for (frame of frames) {
    frame.style.height = (frame.contentWindow.document.body.scrollHeight + 30) + "px";
  }
}