/**
 * script that toggles the class of the <header>
 *  when the user clicks on the tag DIV#toggle_header
 */
$(function () {
  $('#toggle_header').on('click', function () {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      $('header').addClass('green');
    } else {
      $('header').removeClass('green');
      $('header').addClass('red');
    }
  });
});
