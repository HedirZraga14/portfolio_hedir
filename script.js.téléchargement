if (typeof (jQuery) != 'undefined') {

    jQuery.noConflict(); // Reverts '$' variable back to other JS libraries

    (function ($) {
        "use strict";

        $(function () {

            // Counters
            
            function animateCounter() {

                $('.bit-counters-list').each(function(){

                    var counterOffsetBottom     =   $(this).offset().top + $(this).find('.counter-item').height();
                    var windowHeight            =   $(window).height();
                    var scrollAmount            =   $(window).scrollTop();

                    if ( scrollAmount > ( counterOffsetBottom - windowHeight )) {

                        if( $(this).find('.counter-item').length > 0 ){

                            $(this).find('.counter-item').each(function(){
                                $(this).find('.tobe').removeClass('tobe');
                            })

                            $(this).find('.count').each(function() {
                                $(this).prop('Counter', 0).animate({
                                    Counter: $(this).text()
                                }, {
                                    duration: 1000,
                                    easing: 'swing',
                                    step: function(now) {
                                        $(this).text(Math.ceil(now));
                                    }
                                });
                            }); {
                                $(this).find('.count').removeClass('count').addClass('counted');
                            };
                        }
                    }

                })
            }


            $(document).ready(function(){
                
                animateCounter();
                
                $(window).scroll(function() {
                    animateCounter();
                });
            })
            

            // Testimonial Slider
            if ($().slick != undefined) {

                if( $('.bit14-slider').length > 0 ){

                    var slider = $('.bit14-slider');

                    slider.each(function(){

                        var elem = $(this);
                        var arrows = elem.data('arrows') ? true : false;
                        var adaptive_height = elem.data('adaptive-height') ? true : false;
                        var dots = elem.data('dots') ? true : false;
                        var autoplay = elem.data('autoplay') ? true : false;
                        var autoplay_speed = elem.data('autoplay-speed') || 3000;
                        var fade = elem.data('fade') ? true : false;
                        var pause_on_hover = elem.data('pause-onhover') ? true : false;
                        var display_columns = elem.data('display-columns') || 3;
                        var scroll_columns = elem.data('scroll-columns') || 3;
                        var tablet_display_columns = elem.data('tablet-display-columns') || 2;
                        var tablet_scroll_columns = elem.data('tablet-scroll-columns') || 2;
                        var mobile_display_columns = elem.data('mobile-display-columns') || 1;
                        var mobile_scroll_columns = elem.data('mobile-scroll-columns') || 1;

                        elem.slick({
                            arrows: arrows,
                            dots: dots,
                            infinite: true,
                            autoplay: autoplay,
                            adaptiveHeight: adaptive_height,
                            autoplaySpeed: autoplay_speed,
                            fade: fade,
                            pauseOnHover: pause_on_hover,
                            slidesToShow: display_columns,
                            slidesToScroll: scroll_columns,
                            responsive: [
                                {
                                    breakpoint: 800,
                                    settings: {
                                        slidesToShow: tablet_display_columns,
                                        slidesToScroll: tablet_scroll_columns
                                    }
                                },
                                {
                                    breakpoint: 480,
                                    settings: {
                                        slidesToShow: mobile_display_columns,
                                        slidesToScroll: mobile_scroll_columns
                                    }
                                }
                                // You can unslick at a given breakpoint now by adding:
                                // settings: "unslick"
                                // instead of a settings object
                            ]

                        });
                    });
                }
            }

        });



        // Pricing Table
        $(document).ready(function() {
            $('.bit_table_group').each(function(){
                var columns = 'col-md-' + $(this).attr('data-columns') ;
                var primary_color = $(this).attr('data-primary-color');

                $(this).find('.bit_table').each(function(){
                    $(this).addClass(columns);
                    $(this).css('color' , primary_color);
                    $(this).find('.fa-check').css('color' , primary_color);
                    $(this).find('.btn').css('background-color' , primary_color);
                })

            })
        });

        // Newsletter
        $(document).ready(function() {
            $('.newsletter_subscriber').each(function(){
                //Placeholder
                $(this).find('.tnp-email').attr('placeholder' , 'Email Address');

                //Theming
                var theme = $(this).attr('data-theme') ;
                $(this).find('.tnp-email').css('background' , theme);
                $(this).find('.tnp-submit').css('border-color' , theme);
                $(this).find('.tnp-submit').css('color' , theme);

            })
        });

        // Iconic List
        $(document).ready(function(){
            /*$(".bit-iconic-list-item").on({
                mouseenter: function () {
                    var hover_color = $(this).attr('data-hover-color');
                    $(this).css("background-color", hover_color);
                },
                mouseleave: function () {
                    var bg_color = $(this).attr('data-bg-color');
                    $(this).css("background-color", bg_color);
                }

            });*/
        })



    }(jQuery));
}