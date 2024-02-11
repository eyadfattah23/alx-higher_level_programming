/**
 * script that fetches from
 * https://hellosalut.stefanbohacek.dev/?lang=fr
 *  and displays the value of hello
 *  from that fetch in the HTML tag DIV#hello
 */

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    data: 'data',
    dataType: 'json',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
