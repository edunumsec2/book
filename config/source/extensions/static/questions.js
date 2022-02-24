
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
    var feedbacks = question.getElementsByClassName("question-feedback");
    var check_buttons = question.getElementsByClassName("check");
    var show_buttons = question.getElementsByClassName("show");
    var reset_buttons = question.getElementsByClassName("reset");

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

    for (const check_button of check_buttons) {
      check_button.addEventListener("click", check_listener(correct_boxes, incorrect_boxes, check_buttons, feedbacks, question));
    }
    for (const show_button of show_buttons) {
      show_button.addEventListener("click", show_listener(correct_boxes, incorrect_boxes, check_buttons, feedbacks, question));
    }
    for (const reset_button of reset_buttons) {
      reset_button.addEventListener("click", reset_listener(correct_boxes, incorrect_boxes, check_buttons, feedbacks, question));
    }
  }
}

function check_listener(correct_boxes, incorrect_boxes, check_buttons, feedbacks, question) {
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
      for (const feedback of feedbacks) {
        feedback.style.display = "none";
      }
      for (const button of check_buttons) {
        button.disabled = true;
      }
      for (const box of correct_boxes) {
        box.disabled = true;
      }
      for (const box of incorrect_boxes) {
        box.disabled = true;
      }
      question.classList.add("show-answers");
    }
    else {
      create_reaction("bad");
      for (const feedback of feedbacks) {
        feedback.style.display = "block";
      }
    }
  };
}

function show_listener(correct_boxes, incorrect_boxes, check_buttons, feedbacks, question) {
  return function(event) {
    for (const button of check_buttons) {
      button.disabled = true;
    }
    for (const box of correct_boxes) {
      box.checked = true;
      box.disabled = true;
    }
    for (const box of incorrect_boxes) {
      box.checked = false;
      box.disabled = true;
    }
    for (const feedback of feedbacks) {
      feedback.style.display = "block";
    }
    question.classList.add("show-answers");
  };
}

function reset_listener(correct_boxes, incorrect_boxes, check_buttons, feedbacks, question) {
  return function(event) {
    for (const button of check_buttons) {
      button.disabled = false;
    }
    for (const box of correct_boxes) {
      box.checked = false;
      box.disabled = false;
    }
    for (const box of incorrect_boxes) {
      box.checked = false;
      box.disabled = false;
    }
    for (const feedback of feedbacks) {
      feedback.style.display = "none";
    }
    question.classList.remove("show-answers");
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