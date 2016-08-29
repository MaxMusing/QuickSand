$(document).ready(function() {
	$('.tab-window').hide();
	$('.tab-window:eq(0)').show();

	$('.tabbar-button').click(function(e) {
		var pos = $(this).prevAll().length;
		$('.tab-window').hide();
		$('.tab-window:eq(' + pos + ')').show();
		$('.tabbar-button').removeClass('active');
		$(this).addClass('active');
	});
});
