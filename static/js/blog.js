$(document).ready(function() {
  $(".tabs a").click(function(event) {
	var target = $(event.target);

	if (target.is("active")) {
	  // If this is the current tab, no-op
	  event.preventDefault();
	  return;
	}

	$(".tabs .active").toggleClass("active");
	target.parent().toggleClass("active");

	// Find the target for the main frame
	if (target.href == '/') {
	  window.location.hash = "";
	}
	else {
	  window.location.hash = target.href;
	}

	event.preventDefault();
  });
});
