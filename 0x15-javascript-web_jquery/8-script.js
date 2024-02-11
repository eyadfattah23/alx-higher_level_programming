/**
 * script that fetches and lists
 * the title for all movies by using this URL:
 *  https://swapi-api.alx-tools.com/api/films/?format=json
 */

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    data: 'data',
    dataType: 'json',
    success: function (data) {
      $.each(data.results, function (i, movie) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
