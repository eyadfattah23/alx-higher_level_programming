/**
 * script that adds, removes and clears LI elements from a list when the user clicks
 */
document.addEventListener('DOMContentLoaded', function () {
  $(function () {
    const newElement = '<li>Item</li>';
    $('#add_item').on('click', function () {
      $('ul.my_list').append(newElement);
    });
    $('#remove_item').on('click', function () {
      $('ul.my_list li').last().remove();
    });
    $('#clear_list').on('click', function () {
      $('ul.my_list').empty();
    });
  });
});
