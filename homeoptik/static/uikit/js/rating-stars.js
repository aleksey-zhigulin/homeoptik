///**
// * Created by aleksey on 9/24/15.
// */

$().ready(function() {

    $( ".hlinks-rating.One" ).each(function(){
        $(this).find("li").slice(0, 1).toggleClass('active')
    });
    $( ".hlinks-rating.Two" ).each(function(){$(this).find("li").slice(0, 2).toggleClass('active')});
    $( ".hlinks-rating.Three" ).each(function(){$(this).find("li").slice(0, 3).toggleClass('active')});
    $( ".hlinks-rating.Four" ).each(function(){$(this).find("li").slice(0, 4).toggleClass('active')});
    $( ".hlinks-rating.Five" ).each(function(){$(this).find("li").slice(0, 5).toggleClass('active')});

});

