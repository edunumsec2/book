
function questions_ready() {
  var questions = document.getElementsByClassName("question");
  for (const question of questions) {
    var is_mono = true;
    if (question.classList.contains("multi")) {
      is_mono = false;
    }
    else if (question.getElementsByClassName("correct").length != 1) {
      is_mono = false;
    }
    var correct_boxes = [];
    var incorrect_boxes = [];
    var answers = question.getElementsByClassName("answer");
    for (const answer of answers) {
      var correct = answer.classList.contains("correct");
      var box = answer.getElementsByTagName("input").item(0);
      if (correct) {
        correct_boxes.push(box);
      }
      else {
        incorrect_boxes.push(box);
      }
      if (is_mono) {
        box.addEventListener("click", mono_click_listener(answers));
      }
    }
    var check_buttons = question.getElementsByClassName("check");
    for (const check_button of check_buttons) {
      check_button.addEventListener("click", check_listener(correct_boxes, incorrect_boxes))
    }
    var show_buttons = question.getElementsByClassName("show");
    for (const show_button of show_buttons) {
      show_button.addEventListener("click", show_listener(correct_boxes, incorrect_boxes))
    }
  }
}

function check_listener(correct_boxes, incorrect_boxes) {
  return function(event) {
    var correct = true;
    for (const box of correct_boxes) {
      if (!box.checked) {
        correct = false
      }
    }
    for (const box of incorrect_boxes) {
      if (box.checked) {
        correct = false
      }
    }
    if (correct) {
      create_reaction("good");
    }
    else {
      create_reaction("bad");
    }
  };
}

function show_listener(correct_boxes, incorrect_boxes) {
  return function(event) {
    for (const box of correct_boxes) {
      box.checked = true;
    }
    for (const box of incorrect_boxes) {
      box.checked = false;
    }
  };
}

function mono_click_listener(answers) {
  return function(event) {
    for (const answer of answers) {
      var box = answer.getElementsByTagName("input").item(0)
      if (!box.isSameNode(event.target)) {
        box.checked = false;
      }
    }
  };
}

document.addEventListener("DOMContentLoaded", questions_ready, false);