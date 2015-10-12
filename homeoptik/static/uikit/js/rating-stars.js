///**
// * Created by aleksey on 9/24/15.
// */


// Plugin @RokoCB :: Return the visible amount of px
// of any element currently in viewport.
// stackoverflow.com/questions/24768795/
    ;(function($, win) {
        $.fn.inViewport = function(cb) {
            return this.each(function(i,el){
                function visPx(){
                    var H = $(this).height(),
                        r = el.getBoundingClientRect(), t=r.top, b=r.bottom;
                    return cb.call(el, Math.max(0, t>0? H-t : (b<H?b:H)));
                } visPx();
                $(win).on("resize scroll", visPx);
            });
        };
    }(jQuery, window));

$().ready(function() {

    $( ".hlinks-rating.One" ).each(function(){
        $(this).find("li").slice(0, 1).toggleClass('active')
    });
    $( ".hlinks-rating.Two" ).each(function(){$(this).find("li").slice(0, 2).toggleClass('active')});
    $( ".hlinks-rating.Three" ).each(function(){$(this).find("li").slice(0, 3).toggleClass('active')});
    $( ".hlinks-rating.Four" ).each(function(){$(this).find("li").slice(0, 4).toggleClass('active')});
    $( ".hlinks-rating.Five" ).each(function(){$(this).find("li").slice(0, 5).toggleClass('active')});


    $('#voucher_form_link a').inViewport(function(px){
        if(px) $(this).addClass("animated tada") ;
    });
});

