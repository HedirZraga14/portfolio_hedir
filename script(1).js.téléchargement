jQuery(document).ready(function($){
	
	"use strict"; 
	
	$(window).scroll(function(event) {
		$(".me-image > img").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".about-me-info").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".inner-head").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".service").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".about-text-block").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".heading2").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".my-education-sec").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".my-work-sec").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".slider-history").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".history-button").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".testimonials").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".blog").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".wanna-touch").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".main-footer").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".my-name-who").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".services-boxy").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated fadeIn"); 
			} 
		});

		$(".my-skills > .progress > .progress-bar").each(function(i, el) {
			var el = $(el);
			if (el.visible(true)) {
			  el.addClass("animated slideInLeft"); 
			} 
		});

	});
	
	// Get Header Height //
	var stick = $(".inner-page header").height();
	$(".theme-layout").css({
	    "padding-top": stick
	});

	/*** FIXED Menu APPEARS ON SCROLL DOWN ***/	
	$(window).scroll(function() {    
		var scroll = $(window).scrollTop();
		if (scroll >= 50) {
		$("header").addClass("sticky");
		}
		else{
		$("header").removeClass("sticky");
		$("header").addClass("");
		}
	});	

	/*** SMOOTH SCROLLING ***/	
	$(function() {
		$('a[href*="#"]:not([href="#"])').click(function() {
			if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
				var target = $(this.hash);
				target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
				if (target.length) {
				$('html,body').animate({
				scrollTop: target.offset().top
				}, 1000);
				}
			}
		});
	});    


	

	$('.navTrigger').on("click", function(){
	  $(this).toggleClass('active');
	  $(".resume-header").toggleClass("show-menu");
	});	
	

	/*=================== Parallax ===================*/   
	$('.parallax').scrolly({bgParallax: true});
	
});
