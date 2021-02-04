document.addEventListener("DOMContentLoaded", function() {
  var isInterrupted = false;
  var executeBtn = document.getElementById("execute");
  var interruptBtn = document.getElementById("interrupt");
  var canvasArea = document.getElementById("canvas-area");

  function outputFunction(text) {
    var elem = document.getElementById("output");
    elem.innerHTML = elem.innerHTML + text;
  }
  function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
      throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
  }

  var codeElem = CodeMirror.fromTextArea(document.getElementById("code"), {
    lineNumbers: true,
    theme: "monokai",
    indentUnit: 4,
  });

  codeElem.on("change", resized);

  Sk.configure({
    killableWhile: true,
    killableFor: true,
    yieldLimit: 100,
  });

  Sk.onAfterImport = function(library) {
    switch(library) {
      case 'turtle':
        canvasArea.style.display = "block";
        resized();
        break;
    }
  }

  function runInterpreter() {
    canvasArea.style.display = "none";
    executeBtn.disabled = true;
    interruptBtn.disabled = false;
    var prog = codeElem.getValue();
    var elem = document.getElementById("output");
    elem.innerHTML = '';
    Sk.pre = "output";
    Sk.configure({ output: outputFunction, read: builtinRead });
    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'canvas';
    var myPromise = Sk.misceval.asyncToPromise(function() {
      return Sk.importMainWithBody("<stdin>", false, prog, true);
    }, { "*": function () {
      if (isInterrupted) {
        throw "Interruption";
      }
    }});
    myPromise.then(function() {
      executeBtn.disabled = false;
      interruptBtn.disabled = true;
      isInterrupted = false;
    }, function(err) {
      executeBtn.disabled = false;
      interruptBtn.disabled = true;
      isInterrupted = false;
      elem.innerText = elem.innerText + "\n" + err.toString();
    });
  }

  function interruptInterpreter() {
    isInterrupted = true;
  }

  interruptBtn.addEventListener("click", interruptInterpreter);
  executeBtn.addEventListener("click", runInterpreter);

  function resized() {
    if (parent && parent.frameResized) {
      parent.frameResized(self);
    }
  }

  const config = { attributes: false, childList: true, subtree: true };
  const observer = new MutationObserver(resized);
  observer.observe(document.getElementById("output"), config);
  resized();

  if (parent && parent.frameResized) {
    parent.populateFrame(self, codeElem);
  }
});