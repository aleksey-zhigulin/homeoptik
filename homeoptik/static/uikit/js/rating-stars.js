///**
// * Created by aleksey on 9/24/15.
// */

$().ready(function() {

    $( ".hlinks-rating.One" ).find("li").slice(0, 1).toggleClass('active');
    $( ".hlinks-rating.Two" ).find("li").slice(0, 2).toggleClass('active');
    $( ".hlinks-rating.Three" ).find("li").slice(0, 3).toggleClass('active');
    $( ".hlinks-rating.Four" ).find("li").slice(0, 4).toggleClass('active');
    $( ".hlinks-rating.Five" ).find("li").slice(0, 5).toggleClass('active');

});