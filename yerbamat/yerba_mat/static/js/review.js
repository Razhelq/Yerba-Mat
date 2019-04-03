$(function() {

	var butt = $(".btn.btn-success");

	butt.on('click', add_review);

    function add_review() {
        $('.review').css('display', 'inline');
    }
});