/**
 * script that fetches and prints how to say “Hello” depending on the language
 */

document.addEventListener('DOMContentLoaded', function () {
  $(function () {
    function fetchTranslation () {
      const lang = $('INPUT#language_code').val();

      $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
        dataType: 'json',
        success: function (data) {
          $('DIV#hello').text(data.hello);
        },
        error: function (xhr, status, error) {
          // Handle errors here
          console.error('Error:', error);
        }
      });
    }

    // Trigger translation when the button is clicked
    $('INPUT#btn_translate').on('click', function () {
      fetchTranslation();
    });

    // Trigger translation when ENTER is pressed in the language code input field
    $('INPUT#language_code').on('keypress', function (event) {
      if (event.which === 13) {
        fetchTranslation();
      }
    });
  });
});
