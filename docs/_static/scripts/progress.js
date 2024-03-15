document.addEventListener("DOMContentLoaded", function() {

  $("body").append(
    '<svg id="progress-ring">' +
    '<circle class="outer" cx="20" cy="20" r="17" />' +
    '<circle class="progress" cx="20" cy="20" r="17" />' +
    '</svg>');

  var ring = $("#progress-ring .progress")[0];
  var outer = $("#progress-ring .outer")[0];
  var radius = ring.r.baseVal.value;
  var circumference = radius * 2 * Math.PI;

  ring.style.strokeDasharray = "" + circumference + " " + circumference;
  ring.style.strokeDashoffset = "" + circumference;

  function scrollListener() {
    var elem = document.scrollingElement;
    var pos = elem.scrollTop;
    var max = elem.scrollHeight - elem.clientHeight;
    var progress = 1.0;
    if (max > 0) {
      progress = (pos / max);
    }

    var strokeWidth = 6 + 28 * Math.pow(progress, 5);
    ring.style.strokeWidth = strokeWidth;
    outer.style.strokeWidth = strokeWidth;
    ring.style.strokeDashoffset = circumference * (1 - progress);
  }

  scrollListener();

  var supportsPassive = false;
  try {
    var opts = Object.defineProperty({}, 'passive', {
      get: function() {
        supportsPassive = true;
      }
    });
    window.addEventListener("testPassive", null, opts);
    window.removeEventListener("testPassive", null, opts);
  } catch (e) {}
  document.addEventListener("scroll", scrollListener, supportsPassive ? { passive: true } : false);
});