
function random_element(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

var reaction_emoticons = {
  "good": ["😀", "😋"],
  "bad": ["🥵", "🥴"],
};

var reaction_texts = {
  "good": ["Super !", "Bravo !"],
  "bad": ["Oups !", "Aie..."],
};

function setup_reactions() {
  var elem = document.createElement("div");
  $(elem).addClass("reactions");
  $("body").append(elem);
}


function create_reaction(type, text, emoticon) {
  if (typeof type != 'string' || (type != 'good' && type != 'bad')) {
    type = "good";
  }

  if (typeof text == 'undefined') {
    text = random_element(reaction_texts[type]);
  }

  if (typeof emoticon == 'undefined') {
    emoticon = random_element(reaction_emoticons[type]);
  }

  var elem = document.createElement("div");
  $(elem).addClass("reaction");
  $(elem).addClass(type);
  $(elem).append('<span class="emoticon">' + emoticon + '</span>');
  $(elem).append(text);
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