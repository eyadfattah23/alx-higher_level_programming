$(function () {
	$.ajax({
		type: "GET",
		url: "https://swapi-api.alx-tools.com/api/films/?format=json",
		data: "data",
		dataType: "json",
		success: function (response) {
			const list = response.results;
			list.forEach(element => {
				$('#list_movies').append('<li>' + element.title + '</li>');
			});
		}
	});
});
