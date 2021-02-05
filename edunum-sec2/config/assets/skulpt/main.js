document.addEventListener("DOMContentLoaded", function() {
  var isInterrupted = false;
  const executeBtn = document.getElementById("execute");
  const interruptBtn = document.getElementById("interrupt");
  const canvasArea = document.getElementById("canvas-area");
  const canvasElem = document.getElementById("canvas");
  const outputElem = document.getElementById("output");

  function outputFunction(text) {
    const atBottom = outputElem.scrollTop + output.clientHeight >= outputElem.scrollHeight;
    const node = document.createTextNode(text);
    outputElem.appendChild(node);
    if (atBottom) {
      outputElem.scrollTop = outputElem.scrollHeight;
    }
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
    output: outputFunction,
    read: builtinRead,
  });

  Sk.pre = "output";

  Sk.onAfterImport = function(library) {
    switch(library) {
      case 'turtle':
        canvasArea.style.display = "block";
        resized();
        break;
    }
  }

  if (!Sk.TurtleGraphics) {
    Sk.TurtleGraphics = {};
  }
  Sk.TurtleGraphics.target = 'canvas';
  Sk.TurtleGraphics.width = 600;
  Sk.TurtleGraphics.height = 400;
  canvasElem.style.width = "600px";
  canvasElem.style.height = "400px";



  function runInterpreter() {
    canvasArea.style.display = "none";
    executeBtn.disabled = true;
    interruptBtn.disabled = false;
    var prog = codeElem.getValue();
    var elem = document.getElementById("output");
    elem.innerHTML = '';
    
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
      outputFunction(err.toString());
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
    const options = {
      editor: codeElem,
      run: runInterpreter
    };
    parent.populateFrame(self, options);
  }
});