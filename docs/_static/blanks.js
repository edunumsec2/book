
function blanks_ready() {


  var blanks = document.getElementsByClassName("blank")
  for (const blank of blanks) {
    blank.addEventListener("change", function(event) {
      var option = blank.options[blank.selectedIndex];
      var jqObj = $(blank);
      switch (option.value) {
        case '1': // Correct.
          jqObj.addClass('correct_selected');
          jqObj.removeClass('incorrect_selected');
          create_reaction("good");
          break;
        case '0': // Incorrect.
          jqObj.removeClass('correct_selected');
          jqObj.addClass('incorrect_selected');
          create_reaction("bad");
          break;
        default: // Blank.
          jqObj.removeClass('correct_selected');
          jqObj.removeClass('incorrect_selected');
      }
    });
  }
}

document.addEventListener("DOMContentLoaded", blanks_ready, false);