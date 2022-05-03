document.addEventListener("DOMContentLoaded", function() {

  var running = false;

  // Add KeyboardInterrupt exception.
  Sk.builtin.KeyboardInterrupt = function (args) {
    var o;
    if (!(this instanceof Sk.builtin.KeyboardInterrupt)) {
      o = Object.create(Sk.builtin.KeyboardInterrupt.prototype);
      o.constructor.apply(o, arguments);
      return o;
    }
    Sk.builtin.BaseException.apply(this, arguments);
  };
  Sk.abstr.setUpInheritance("KeyboardInterrupt", Sk.builtin.KeyboardInterrupt, Sk.builtin.BaseException);

  const copyBtn = document.getElementById("copy");
  const executeBtn = document.getElementById("execute");
  const interruptBtn = document.getElementById("interrupt");
  const downloadBtn = document.getElementById("download");
  const hintsBtn = document.getElementById("hints");
  const hintsArea = document.getElementById("tooltip");
  const hintsElem = document.getElementById("tooltip-content");
  const canvasArea = document.getElementById("canvas-area");
  const canvasElem = document.getElementById("canvas");
  const outputElem = document.getElementById("output");
  const outputArea = document.getElementById("output-area");
  const outputDefaultMessage = document.getElementById("output-message");

  var downloadFileName = "code.py";
  var prelude = "";
  var preludeLines = 0;
  var afterword = "";
  var afterwordLines = 0;
  var code = "";
  var codeLines = 0;
  var hints = [];
  var readOnly = false;
  var alwaysShowOutput = false;
  var alwaysHideOutput = false;
  var includePreludeInDownload = true;
  var includeAfterwordInDownload = true;

  var rejectInput = null;

  function outputElement(elem) {
    if (!alwaysHideOutput) {
      outputArea.style.display = "block";
    }
    outputDefaultMessage.style.display = "none";
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
    theme: "idea",
    indentUnit: 4,
    indentWithTabs: false,
    smartIndent: true,
    extraKeys: {
      'Shift-Enter': runInterpreter,
      'Cmd-Enter': runInterpreter,
      'Ctrl-Enter': runInterpreter,
      Tab: function(cm) {
        if (cm.getMode().name === 'null') {
          cm.execCommand('insertTab');
        } else {
          if (cm.somethingSelected()) {
            cm.execCommand('indentMore');
          } else {
            cm.execCommand('insertSoftTab');
          }
        }
      },
      'Shift-Tab': function(cm) { cm.execCommand('indentLess'); }
    },
  });

  function setTheme(theme) {
    if (theme === "dark" || theme === "auto" && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      codeElem.setOption('theme', "monokai");
    }
    else {
      codeElem.setOption('theme', "idea");
    }
  }

  function refreshTheme() {
    theme = document.body.dataset.theme || "auto";
    setTheme(theme);
  }
  document.refreshTheme = refreshTheme;

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', refreshTheme);

  codeElem.on("change", resized);

  Sk.configure({
    killableWhile: true,
    killableFor: true,
    yieldLimit: 100,
    output: outputFunction,
    read: builtinRead,
    inputfun: inputFunction,
    inputfunTakesPrompt: true,
    __future__: Sk.python3,
  });

  Sk.pre = "output";

  Sk.onAfterImport = function(library) {
    switch(library) {
      case 'turtle':
        canvasArea.style.display = "block";
        if (!alwaysShowOutput) {
          outputArea.style.display = "none";
        }
        resizeCanvas();
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

  function resizeCanvas() {
    const availableWidth = canvasArea.clientWidth - 26;
    if (availableWidth < 0) {
      return;
    }
    const targetWidth = 600;
    const targetHeight = 400;

    if (availableWidth < targetWidth) {
      const ratio = availableWidth / targetWidth;
      canvasElem.style.transform = "scale(" + ratio + ")";
      canvasArea.style.height = (targetHeight * ratio + 6) + "px";
    }
    else {
      canvasArea.style.height = (targetHeight + 6) + "px";
    }
    resized();
  }

  window.addEventListener("resize", resizeCanvas);

  function errorToString(err) {
    var msg = err.tp$name + ": " + err.tp$str().v;

    if (err.traceback.length > 0) {
      const firstFrame = err.traceback[0];
      if (firstFrame.filename === "<stdin>.py" &&
          firstFrame.lineno > preludeLines &&
          firstFrame.lineno <= preludeLines + codeLines) {
        // Error located in user code.
        msg += " on line " + (firstFrame.lineno - preludeLines);
      }
      else {
        // Error in library code.
        msg += " in a library call";
        // Try to find user frame.
        var i = 1; // Set to 1 as we skip first frame.
        while (i < err.traceback.length) {
          const frame = err.traceback[i];
          if (frame.filename === "<stdin>.py" &&
              frame.lineno > preludeLines) {
            msg += " originating from line " + (frame.lineno - preludeLines);
            break;
          }
          i += 1;
        }
      }
    }

    msg += ".";

    return msg;
  }

  function runInterpreter() {
    if (running) {
      return;
    }
    running = true;
    outputDefaultMessage.innerText = "Aucune sortie à afficher.";
    outputDefaultMessage.style.display = "block";
    canvasArea.style.display = "none";
    executeBtn.disabled = true;
    interruptBtn.disabled = false;
    codeElem.setOption("readOnly", "nocursor")
    code = codeElem.getValue();
    codeLines = code.split("\n").length;
    const prog = prelude + code + afterword;
    outputElem.innerHTML = '';
    outputDefaultMessage.classList.remove("shine");
    void outputDefaultMessage.offsetWidth;
    outputDefaultMessage.classList.add("shine");
    outputElem.classList.remove("shine");
    void outputElem.offsetWidth;
    outputElem.classList.add("shine");
    executeBtn.classList.remove("shine");
    void executeBtn.offsetWidth;
    executeBtn.classList.add("shine");
    
    var myPromise = Sk.misceval.asyncToPromise(function() {
      return Sk.importMainWithBody("<stdin>", false, prog, true);
    }, { "*": function () {
      if (Sk.hardInterrupt === true) {
        throw new Sk.builtin.KeyboardInterrupt("interrupted");
      } else {
        return null;
      }
    }});
    myPromise.then(function() {
      executeBtn.disabled = false;
      interruptBtn.disabled = true;
      Sk.hardInterrupt = false;
      if (!readOnly) {
        codeElem.setOption("readOnly", false);
      }
      running = false;
    }, function(err) {
      executeBtn.disabled = false;
      interruptBtn.disabled = true;
      Sk.hardInterrupt = false;
      if (!readOnly) {
        codeElem.setOption("readOnly", false);
      }
      running = false;

      outputFunction(errorToString(err));
    });
  }

  function interruptInterpreter() {
    Sk.hardInterrupt = true;
    if (rejectInput != null) {
      rejectInput();
    }
  }

  var clipboard = new ClipboardJS('#copy', {
      text: function(trigger) {
          let data = codeElem.getValue();
          if (includePreludeInDownload) {
            data = prelude + "\n" + data;
          }
          if (includeAfterwordInDownload) {
            data += "\n" + afterword;
          }
          return data;
      }
  });

  clipboard.on('success', function(e) {
      if (parent && parent.create_reaction) {
        parent.create_reaction('good', 'Copié !');
      }
      e.clearSelection();
  });

  interruptBtn.addEventListener("click", interruptInterpreter);
  executeBtn.addEventListener("click", runInterpreter);
  document.getElementById("execute-keyword").addEventListener("click", runInterpreter);

  // Courtesy of https://stackoverflow.com/a/33542499
  function saveFile(filename, data) {
    const blob = new Blob([data], {type: 'text/x-python'});
    if(window.navigator.msSaveOrOpenBlob) {
      window.navigator.msSaveBlob(blob, filename);
    }
    else{
      const elem = window.document.createElement('a');
      elem.href = window.URL.createObjectURL(blob);
      elem.download = filename;        
      document.body.appendChild(elem);
      elem.click();        
      document.body.removeChild(elem);
      window.URL.revokeObjectURL(elem.href);
    }
  }

  downloadBtn.addEventListener("click", function() {
    var data = codeElem.getValue();
    if (includePreludeInDownload) {
      data = prelude + "\n" + data;
    }
    if (includeAfterwordInDownload) {
      data += "\n" + afterword;
    }
    saveFile(downloadFileName, data);
  });

  function resized() {
    if (parent && parent.frameResized) {
      parent.frameResized(self);
    }
  }

  const config = { attributes: false, childList: true, subtree: true };
  const observer = new MutationObserver(resized);
  observer.observe(document.getElementById("output"), config);
  resized();

  // Courtesy of https://stackoverflow.com/questions/30106476/using-javascripts-atob-to-decode-base64-doesnt-properly-decode-utf-8-strings
  function b64DecodeUnicode(str) {
    return decodeURIComponent(atob(str).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
  }

  var popperInstance = null;
  function createTooltip() {
    hintsArea.style.display = "block";
    popperInstance = Popper.createPopper(hintsBtn, hintsArea, {
      modifiers: [
        {
          name: 'offset',
          options: {
            offset: [0, 8],
          },
        },
      ],
    });
  }

  function hideTooltip() {
    hintsArea.style.display = "none";
    popperInstance.destroy();
    popperInstance = null;
  }

  hintsBtn.addEventListener("click", function () {
    if (popperInstance == null) {
      createTooltip();
    }
    else {
      hideTooltip();
    }
  });

  hintsElem.addEventListener("click", function () {
    nextHint();
  });

  document.addEventListener("click", function(e) {
    if (popperInstance != null && !hintsBtn.contains(e.target) && !hintsArea.contains(e.target)) {
      hideTooltip();
    }
  });

  var loadedHint = -1;
  function loadHint(index) {
    loadedHint = index;
    hintsElem.innerText = hints[index];
  }

  function nextHint() {
    loadHint((loadedHint + 1) % hints.length);
    if (popperInstance != null) {
      hideTooltip();
    }
    createTooltip();
  }
  function initialise() {
    if (!parent.frameResized) {
      setTimeout(initialise, 100);
      return;
    }
    parent.populateFrame(self, function(frame) {
      codeElem.setValue(b64DecodeUnicode(frame.dataset.code));
      if (frame.hasAttribute("data-prelude")) {
        const rawPrelude = b64DecodeUnicode(frame.dataset.prelude);
        prelude = rawPrelude + "\n";
        preludeLines = rawPrelude.split("\n").length;
      }
      if (frame.hasAttribute("data-afterword")) {
        const rawAfterword = b64DecodeUnicode(frame.dataset.afterword);
        afterword = "\n" + rawAfterword;
        afterwordLines = rawAfterword.split("\n").length;
      }
      if (frame.hasAttribute("data-hints")) {
        const rawHints = frame.dataset.hints.split(" ");
        for (const hint of rawHints) {
          hints.push(b64DecodeUnicode(hint));
        }
        loadHint(0);
        hintsBtn.disabled = false;
      }
      if (frame.hasAttribute("data-nocontrols")) {
        document.getElementById("control-area").style.display = "none";
      }
      if (frame.hasAttribute("data-static")) {
        codeElem.setOption("readOnly", true);
        readOnly = true;
      }
      if (frame.hasAttribute("data-download-hide-prelude")) {
        includePreludeInDownload = false;
      }
      if (frame.hasAttribute("data-download-hide-afterword")) {
        includeAfterwordInDownload = false;
      }
      if (frame.hasAttribute("data-file")) {
        downloadFileName = b64DecodeUnicode(frame.dataset.file);
      }
      if (frame.hasAttribute("data-output-min-lines")) {
        const minLines = parseInt(frame.dataset.outputMinLines);
        outputElem.style.minHeight = minLines * 1.3 + "em";
        outputArea.style.minHeight = (minLines * 1.3 + 2) + "em";
        if (minLines > 0) {
          alwaysShowOutput = true;
        }
      }
      if (frame.hasAttribute("data-output-max-lines")) {
        const maxLines = parseInt(frame.dataset.outputMaxLines);
        outputElem.style.maxHeight = maxLines * 1.3 + "em";
        outputArea.style.maxHeight = (maxLines * 1.3 + 2) + "em";
        if (maxLines === 0) {
          alwaysHideOutput = true;
          outputArea.style.display = "none";
        }
      }

      resized();
      refreshTheme();

      if (frame.hasAttribute("data-run")) {
        runInterpreter()
      }
    });
  }

  if (parent) {
    initialise();
  }
});