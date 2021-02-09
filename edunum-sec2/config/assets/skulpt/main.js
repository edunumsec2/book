document.addEventListener("DOMContentLoaded", function() {
  var isInterrupted = false;
  const executeBtn = document.getElementById("execute");
  const interruptBtn = document.getElementById("interrupt");
  const canvasArea = document.getElementById("canvas-area");
  const canvasElem = document.getElementById("canvas");
  const outputElem = document.getElementById("output");
  var inputElem = null;
  var rejectInput = null;

  function outputElement(elem) {
    const atBottom = outputElem.scrollTop + output.clientHeight >= outputElem.scrollHeight;
    outputElem.appendChild(elem);
    if (atBottom) {
      outputElem.scrollTop = outputElem.scrollHeight;
    }
  }

  function outputFunction(text) {
    const node = document.createTextNode(text);
    outputElement(node);
  }

  function inputFunction(prompt) {
    return new Promise(function(resolve, reject) {
        const node = document.createElement("div");
        const box = document.createElement("input");
        const text = document.createTextNode(prompt);
        const send = document.createElement("button");
        send.type = "button";
        send.innerText = "↵";
        send.className = "btn btn-primary";
        node.appendChild(text);
        node.appendChild(box);
        node.appendChild(send);
        const hideBox = function() {
          const answer = box.value;
          const replacement = document.createElement("span");
          replacement.innerText = answer;
          replacement.className = "user-input";
          node.replaceChild(replacement, box);
          node.removeChild(send);
          inputElem = null;
          rejectInput = null;
        };
        const validate = function() {
          const answer = box.value;
          hideBox();
          resolve(answer);
        };
        send.addEventListener("click", validate);
        box.addEventListener("keypress", function(event) {
          if(event.key == "Enter") {
            validate();
          }
        });
        outputElement(node);
        inputElem = box;
        rejectInput = function() {
          hideBox();
          reject();
        };
        box.focus();
    });
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
    inputfun: inputFunction,
    inputfunTakesPrompt: true,
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
    if (rejectInput != null) {
      rejectInput();
    }
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