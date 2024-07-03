document.addEventListener('DOMContentLoaded', function () {

	function get_hello() {
		const lang = $('INPUT#language_code').val()

		$.ajax({
			type: "GET",
			url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lang,
			data: "data",
			dataType: "json",
			success: function (data) {
				$('div#hello').text(data.hello);
			},
			error: function (xhr, status, error) {
				// Handle errors here
				console.error('Error:', error);
			}
		});
	}
	$(function () {
		$('INPUT#btn_translate').on('click', function () {
			get_hello();
		});

		$('#language_code').on('keypress', function (e) {
			if (e.which == 13) {
				get_hello();
			}
		})
	})
});
