/*=================================================================

Template name: Sofast Multipurpose eCommerce HTML Template
Version: 1.0.0
Author: SITL     
Author url: https://www.sitlbd.com/
Developer: Najmul Huda Eimon

[Table of Content]

01: Preloader
02: Background image
03: mobile Menu
04: Sticky menu
05: Scroll to top button
06: fancybox
07: menu ad slider
08: packery home 1
09: countdown
10: Venobox video play
11: menu ad slider
12: shop page range slider
13: Select style
14: input spinner
15: star rating
16: product details slider
17: product details slider tab
18: contact page Google Map
 
====================================================================*/

$(function() {
    "use strict";

    /*================================================================
      01: Preloader
    =================================================================*/
    $(document).ready(function() {
        setTimeout(() => {
            $('.preloader').fadeOut();
        }, 250)
    });

    /*=====================================================================
        02: Background image
    ======================================================================*/
    let imageTarget = $('[data-img]');
    imageTarget.css('background', function() {
        return 'url(' + this.getAttribute('data-img') + ') no-repeat center'
    });
    imageTarget.css('backgroundSize', 'cover');

    /*=====================================================================
        03: mobile Menu
    ======================================================================*/
    $('.header-menu a[href="#"]').on("click", function(e) {
        e.preventDefault();
    });

    $(".header-menu").menumaker({ title: '<i class="fas fa-bars"></i>', format: "multitoggle" });


    /*=====================================================================
        04: Sticky menu
    ======================================================================*/
    function menuSticky() {
        var $scroll = $(window).scrollTop();
        if ($scroll > 120) {
            $('.menubar').addClass('sticky');
        } else {
            $('.menubar').removeClass('sticky');
        }
    }
    menuSticky()
    $(window).on('scroll', function() {
        menuSticky()

    });

    /*=====================================================================
        05: Scroll to top button
    =======================================================================*/

    $('.top-to-btn').on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: 0
        }, 400);
    });


    $(window).on('scroll', function() {
        var $scroll = $(this).scrollTop();

        if ($scroll > 300) {
            $('.scroll-top').addClass('show');
        } else {
            $('.scroll-top').removeClass('show');
        }
    });

    /*=============================================================
    06: fancybox
    =============================================================*/
    $(window).on('load', function() {
        if ($('.fancybox').length !== 0) {
            setTimeout(function() {
                $('.fancybox').addClass('window-show');
                $('body').delay(500).addClass('window-open');
            }, 3000);
        }
    })

    function modalfunction() {
        $('.close-fancy').on('click', function() {
            $('.fancybox').removeClass('window-show');
            $('body').removeClass('window-open');
        })
        $('.fancybox-bg').on('click', function() {
            $(this).fadeTo(1000, 0);
            $('.fancybox-content').delay(500).parent().removeClass('window-show');
            $('body').removeClass('window-open');
        })

    }
    modalfunction()

    /*=====================================================================
        07: menu ad slider
    ======================================================================*/
    var swiper = new Swiper('.ad-slider', {
        observer: true,
        observeParents: true,
        loop: true,
        centeredSlides: false,
        spaceBetween: 0,

        // effect: 'cube',
        // grabCursor: false,
        // cubeEffect: {
        //     shadow: true,
        //     slideShadows: true,
        //     shadowOffset: 20,
        //     shadowScale: 0.94,
        // },
        disableOnInteraction: false,
        autoplay: false,
        slidesPerView: 1,
        autoplay: {
            delay: 2000,
        },
        breakpoints: {
            1920: {
                slidesPerView: 1,
            },
            992: {
                slidesPerView: 1,
            },
            768: {
                slidesPerView: 1,
            },
            576: {
                slidesPerView: 1,
            },
            320: {
                slidesPerView: 1,
            }
        }

    });

    /*================================================
        08: packery home 1
    ================================================*/
    $(document).ready(function() {
        categoryLayout()
    });
    $(window).on('load', function() {
        categoryLayout()
    });
    const categoryLayout = () => {
        return $('.grid').packery({
            itemSelector: '.grid-item'
        });
    }
    categoryLayout()
        /*=============================================================
            09: countdown
        ==============================================================*/
    $('#offer-time').countdown('2022/01/01', function(event) {
        let week = event.strftime('%w')
        let day = event.strftime('%d')
        $(this).find('ul li .days').html((week * 7) + parseFloat(day))
        $(this).find('ul li .hours').html(event.strftime('%H'))
        $(this).find('ul li .minutes').html(event.strftime('%M'))
        $(this).find('ul li .secounds').html(event.strftime('%S'))
    });

    /*=====================================================================
        10: Venobox video play
    ======================================================================*/
    $('.venobox').venobox({
        spinner: 'cube-grid'
    });

    /*=====================================================================
        11: menu ad slider
    ======================================================================*/
    var swiper = new Swiper('.category-slider', {
        observer: true,
        observeParents: true,
        loop: true,
        centeredSlides: false,
        spaceBetween: 10,
        disableOnInteraction: false,
        autoplay: false,
        slidesPerView: 6,
        autoplay: {
            delay: 2000,
        },
        breakpoints: {
            1920: {
                slidesPerView: 6,
            },
            992: {
                slidesPerView: 4,
            },
            768: {
                slidesPerView: 4,
            },
            576: {
                slidesPerView: 3,
            },
            320: {
                slidesPerView: 1,
            }
        },
        navigation: {
            nextEl: '.btn-next',
            prevEl: '.btn-prev',
        }

    });


    /*=====================================================================
        12: shop page range slider
    ======================================================================*/

    // Product Quantity
    $("#slider-range").slider({
        range: true,
        min: 0,
        max: 300,
        values: [0, 200],
        slide: function(event, ui) {
            $("#amount").val("تومان" + ui.values[0] + " - تومان" + ui.values[1]);
        }
    });
    $("#amount").val("تومان" + $("#slider-range").slider("values", 0) +
        " - تومان" + $("#slider-range").slider("values", 1));


    /*=====================================================================
    13: Select style
   ======================================================================*/
    $(".select").select2({
        width: 'resolve'
    });

    /*=====================================================================
        14: input spinner
    ======================================================================*/

    $('.number-spinner button').on('click', function(e) {
        e.preventDefault()
        var btn = $(this),
            oldValue = btn.closest('.number-spinner').find('input').val(),
            newVal = 0;

        if (btn.attr('data-dir') == 'up') {
            newVal = parseInt(oldValue) + 1;
        } else {
            if (oldValue > 1) {
                newVal = parseInt(oldValue) - 1;
            } else {
                newVal = 1;
            }
        }
        btn.closest('.number-spinner').find('input').val(newVal);
    });

    /*=====================================================================
        15: star rating
    ======================================================================*/

    $('#stars li').on('mouseover', function() {
        var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on

        /* 2. Action to perform on click */
        $('#stars li').on('click', function() {
            var onStar = parseInt($(this).data('value'), 10); // The star currently selected
            var stars = $(this).parent().children('li.star');

            for (var i = 0; i < stars.length; i++) {
                $(stars[i]).removeClass('selected');
            }

            for (var i = 0; i < onStar; i++) {
                $(stars[i]).addClass('selected');
            }

        });


    });

    /*==============================================================
    16: product details slider
    ================================================================*/
    let $productGallery = $('.product-gallery'),
        $productThumbs = $('.product-thumb');


    let productPreview = new Swiper('.product-gallery', {
        observer: true,
        observeParents: true,
        spaceBetween: 1,
        touchRatio: 0,
        effect: "fade",
        pagination: {
            el: '.product-gallery-pagination',
            clickable: true,
        }
    });

    let productThumbs = new Swiper('.product-thumb', {
        observer: true,
        observeParents: true,
        spaceBetween: 30,
        slidesPerView: 4,
        slideToClickedSlide: true,
        slidesPerView: 3,
    });

    $('.product-gallery .swiper-slide-active img').elevateZoom({
        zoomType: "inner",
        lensShape: "round",
        lensSize: 200,
        zoomWindowFadeIn: 500,
        zoomWindowFadeOut: 500
    });


    $productThumbs.on('click', '.swiper-slide', function(event) {
        var $t = $(this);
        console.log($t);
        productPreview.slideTo($t.index());
        $t.addClass('active swiper-slide-active').siblings().removeClass('active swiper-slide-active');
        $('.product-gallery .swiper-slide-active img').elevateZoom({
            zoomType: "inner",
            cursor: "crosshair",
            zoomWindowFadeIn: 500,
            zoomWindowFadeOut: 500
        });
    });


    /*==============================================================
    17: product details slider tab
    ================================================================*/
    let $productGalleryTab = $('.product-gallery-tab'),
        $productThumbsTab = $('.product-thumb-tab');


    let productPreviewTab = new Swiper('.product-gallery-tab', {
        spaceBetween: 1,
        touchRatio: 0,
        effect: 'fade',
        pagination: {
            el: '.product-gallery-pagination',
            clickable: true,
        }
    });

    let productThumbsTab = new Swiper('.product-thumb-tab', {
        spaceBetween: 10,
        slidesPerView: 4,
        slideToClickedSlide: true,
        slidesPerView: 3,
        direction: 'vertical',
    });
    $('.product-gallery-tab .swiper-slide-active img').elevateZoom({
        zoomType: "inner",
        lensShape: "round",
        lensSize: 200,
        zoomWindowFadeIn: 500,
        zoomWindowFadeOut: 500
    });

    $productThumbsTab.on('click', '.swiper-slide', function(event) {
        var $t = $(this);
        productPreviewTab.slideTo($t.index());
        $t.addClass('active swiper-slide-active').siblings().removeClass('active swiper-slide-active');
        $('.product-gallery-tab .swiper-slide-active img').elevateZoom({
            zoomType: "inner",
            lensShape: "round",
            lensSize: 200,
            zoomWindowFadeIn: 500,
            zoomWindowFadeOut: 500
        });

    });

    /*=========================================================
    18: contact page Google Map
    ==========================================================*/

    if ($('#map').length !== 0) {

        var googleMapSelector = $('#map');
        var latitude = $('.google-map-wrapper').attr('data-latitude');
        var longitude = $('.google-map-wrapper').attr('data-longitude');
        var zoome = $('.google-map-wrapper').attr('data-zoom');
        var zoomtoNum = Number(zoome);
        var mapmarker = $('.google-map-wrapper').attr('data-marker');
        var myCenter = new google.maps.LatLng(latitude, longitude);

        function initialize() {
            var mapProp = {
                center: myCenter,
                zoom: zoomtoNum,
                scrollwheel: false,
                mapTypeId: google.maps.MapTypeId.ROADMAP,
                styles: [{
                        "featureType": "landscape.man_made",
                        "elementType": "geometry",
                        "stylers": [{
                            "color": "#f7f1e0"
                        }]
                    },
                    {
                        "featureType": "landscape.natural",
                        "elementType": "geometry",
                        "stylers": [{
                            "color": "#d0e3b4"
                        }]
                    },
                    {
                        "featureType": "landscape.natural.terrain",
                        "elementType": "geometry",
                        "stylers": [{
                            "visibility": "off"
                        }]
                    },
                    {
                        "featureType": "poi",
                        "elementType": "labels",
                        "stylers": [{
                            "visibility": "off"
                        }]
                    },
                    {
                        "featureType": "poi.business",
                        "elementType": "all",
                        "stylers": [{
                            "visibility": "off"
                        }]
                    },
                    {
                        "featureType": "poi.medical",
                        "elementType": "geometry",
                        "stylers": [{
                            "color": "#fbd3da"
                        }]
                    },
                    {
                        "featureType": "poi.park",
                        "elementType": "geometry",
                        "stylers": [{
                            "color": "#bde6ab"
                        }]
                    },
                    {
                        "featureType": "road",
                        "elementType": "geometry.stroke",
                        "stylers": [{
                            "visibility": "off"
                        }]
                    },
                    {
                        "featureType": "road",
                        "elementType": "labels",
                        "stylers": [{
                            "visibility": "off"
                        }]
                    },
                    {
                        "featureType": "road.highway",
                        "elementType": "geometry.fill",
                        "stylers": [{
                            "color": "#ffe36f"
                        }]
                    },
                    {
                        "featureType": "road.highway",
                        "elementType": "geometry.stroke",
                        "stylers": [{
                            "color": "#efd151"
                        }]
                    },
                    {
                        "featureType": "road.arterial",
                        "elementType": "geometry.fill",
                        "stylers": [{
                            "color": "#ffffff"
                        }]
                    },
                    {
                        "featureType": "road.local",
                        "elementType": "geometry.fill",
                        "stylers": [{
                            "color": "black"
                        }]
                    },
                    {
                        "featureType": "transit.station.airport",
                        "elementType": "geometry.fill",
                        "stylers": [{
                            "color": "#cfb2db"
                        }]
                    },
                    {
                        "featureType": "water",
                        "elementType": "geometry",
                        "stylers": [{
                            "color": "#a2daf2"
                        }]
                    }
                ]
            };
            var map = new google.maps.Map(document.getElementById('map'), mapProp);
            var marker = new google.maps.Marker({
                position: myCenter,
                icon: mapmarker,
            });
            marker.setMap(map);


        }
        if (googleMapSelector.length) {
            google.maps.event.addDomListener(window, 'load', initialize);
        }
    }




});