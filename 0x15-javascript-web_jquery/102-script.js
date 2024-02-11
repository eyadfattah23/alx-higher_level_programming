/**
 * script that fetches and prints how to say “Hello” depending on the language
 */

document.addEventListener('DOMContentLoaded', function () {
  $(function () {
    $('INPUT#btn_translate').on('click', function () {
      const lang = $('INPUT#language_code').val();

      $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
        data: 'data',
        dataType: 'json',
        success: function (data) {
          $('DIV#hello').text(data.hello);
        },
        error: function (xhr, status, error) {
          // Handle errors here
          console.error('Error:', error);
        }
      });
    });
  });
});
