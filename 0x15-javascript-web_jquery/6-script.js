/** script that updates the text of the <header>
 *  to New Header!!! when the user clicks on DIV#update_header */

$(function () {
  $('#update_header').on('click', function () {
    $('header').text('New Header!!!');
  });
});
