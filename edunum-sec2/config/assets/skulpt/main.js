document.addEventListener("DOMContentLoaded", function() {
  function outputFunction(text) {
    var elem = document.getElementById("output");
    elem.innerHTML = elem.innerHTML + text;
  }
  function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
      throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
  }

  var codeElem = CodeMirror.fromTextArea(document.getElementById("code"), {lineNumbers:true});

  function runInterpreter() {
    var prog = codeElem.getValue();
    var elem = document.getElementById("output");
    elem.innerHTML = '';
    Sk.pre = "output";
    Sk.configure({ output: outputFunction, read: builtinRead });
    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'canvas';
    var myPromise = Sk.misceval.asyncToPromise(function () {
      return Sk.importMainWithBody("<stdin>", false, prog, true);
    });
    myPromise.then(function (mod) {
      console.log('success');
    },
      function (err) {
        console.log(err.toString());
      });
  }

  document.getElementById("execute").addEventListener("click", runInterpreter);
});