
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
      frame.contentDocument.body.dataset.theme = document.body.dataset.theme;
      initialise(frame);
    }
  }
}

document.addEventListener("DOMContentLoaded", function() {
  const buttons = document.getElementsByClassName("theme-toggle");
  const frames = document.getElementsByClassName("codeframe");
  
  for (const button of buttons) {
    button.addEventListener("click", function() {
      const theme = document.body.dataset.theme;
      console.log(theme);
      for (const frame of frames) {
        const innerDoc = frame.contentDocument;
        innerDoc.body.dataset.theme = theme;
        innerDoc.refreshTheme();
      }
    });
  }
});