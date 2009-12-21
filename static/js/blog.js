$(document).ready(function() {
  $(".tabs a").click(function(event) {
	var target = $(event.target);
	var link = $(target.href);

	if (!target.is("active")) {
	  $(".tabs li.active").toggleClass("active");
	  target.parent().toggleClass("active");
	}

	event.preventDefault();
  });
});