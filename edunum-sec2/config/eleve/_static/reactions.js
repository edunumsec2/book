
function setup_reactions() {
  var elem = document.createElement("div");
  $(elem).addClass("reactions");
  $("body").append(elem);
}

function create_reaction(text, type) {
  var elem = document.createElement("div");
  $(elem).addClass("reaction");
  if (type) {
    $(elem).addClass(type);
  }
  $(elem).text(text);
  $(".reactions").prepend(elem);
  $(elem).animate({opacity: "1"}, 250, "linear");
  setTimeout(hide_reaction(elem), 1500);
}

function hide_reaction(elem) {
  return function() {
    $(elem).animate({marginTop: "200px", opacity: "0"}, 750, "linear", function() {
      $(elem).remove();
    });
  };
}

document.addEventListener("DOMContentLoaded", setup_reactions, false);