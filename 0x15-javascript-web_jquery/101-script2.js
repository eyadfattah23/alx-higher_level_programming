document.addEventListener('DOMContentLoaded', function () {
	$(function () {
		const item = '<li>Item</li>';

		$('#add_item').on('click', function () {
			$('.my_list').append(item);
		});
		$('#remove_item').on('click', function () {
			$('.my_list li:last-child').remove();
		});

		$('#clear_list').on('click', function () {
			$('.my_list').empty();
		});


	})
})
