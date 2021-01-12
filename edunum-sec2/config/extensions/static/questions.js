
function ready() {
  var questions = document.getElementsByClassName("question");
  for (const question of questions) {
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
    }
    var check_buttons = question.getElementsByClassName("check");
    for (const check_button of check_buttons) {
      check_button.addEventListener("click", check_listener(correct_boxes, incorrect_boxes))
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
    alert(correct ? "Bravo!" : "Oups!");
  };
}

document.addEventListener("DOMContentLoaded", ready, false);