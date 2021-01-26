document.addEventListener("DOMContentLoaded", function() {

  $("body").append(
    '<svg id="progress-ring">' +
    '<circle class="outer" cx="20" cy="20" r="17" />' +
    '<circle class="progress" cx="20" cy="20" r="17" />' +
    '</svg>');

  var ring = $("#progress-ring .progress")[0];
  var radius = ring.r.baseVal.value;
  var circumference = radius * 2 * Math.PI;

  ring.style.strokeDasharray = "" + circumference + " " + circumference;
  ring.style.strokeDashoffset = "" + circumference;

  function scrollListener(event) {
    var elem = document.scrollingElement;
    var pos = elem.scrollTop;
    var max = elem.scrollHeight - elem.clientHeight;
    var progress = (pos / max);

    ring.style.strokeWidth = 6 + 28 * Math.pow(progress, 3);
    ring.style.strokeDashoffset = circumference * (1 - progress);
  }

  document.addEventListener("scroll", scrollListener);
});