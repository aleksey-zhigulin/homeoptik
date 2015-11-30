/* ============================================================================
  - Description : Theme utility functions
============================================================================= */
// UTILS
// -------------------------------------------------
var htmlMap = {"&": "&amp;","<": "&lt;",">": "&gt;",'"': '&quot;',"'": '&#39;',"/": '&#x2F;'};

function toJsonFormat(str) {
  str = str.replace(/([a-zA-Z0-9]+?):/g, '"$1":');
  str= str.replace(/:(?!true|false)([a-zA-Z]+)/g, ':"$1"');
  str = str.replace(/'/g, '"');
  return str;
}

function jsonify(str) {
  str = toJsonFormat(str);
  return jQuery.parseJSON(str);
}

function escapeHtml(string) {
  return String(string).replace(/[&<>"'\/]/g, function (s) {
    return htmlMap[s];
  });
}

// PRELOADER
// -------------------------------------------------
$(window).load(function() {
  $('.page-preloader .anim').fadeOut(); 
  $('.page-preloader').delay(350).fadeOut();
  $('body').delay(350).queue(function() {
    $(this).removeClass("preload");
  });
})


$().ready(function() {

  /* NAV TOGGLER
  // ------------------------------------------------- */
  var triggerH = $(".nav-top").height() + $(".main-header").height();
  var toggleEl = $(".nav-bottom");
  
  function autoToggleNav() {
    triggerH = $(".nav-top").height() + $(".main-header").height();
    var toggleClass = "fixed";
    
    if($(window).width() > 767 && window['dontToggle'] == undefined) {
      if (window.scrollY > triggerH) {
        toggleEl.addClass(toggleClass);
      } else {
        toggleEl.removeClass(toggleClass);
      }
    }
    

  }
  
  autoToggleNav();
  
  $(window).scroll(function() {
    autoToggleNav();

  });
  
  // rare moments when switching between screens
  $(window).resize(function() {
    autoToggleNav();
  });
  
  // PRETTY PHOTO
  // -------------------------------------------------
  $("a[data-gal^='prettyPhoto']").prettyPhoto({hook:'data-gal', overlay_gallery:false, social_tools:false});
  
  // CODE FORMATTER
  // -------------------------------------------------
  $(".format-code").each(function() {
    var cleanHtml = escapeHtml($(this).html());
    $(this).html(cleanHtml);
  });
  
  $(".hl-code").each(function(i, block) {
    hljs.highlightBlock(block);
  });
  
  // UL TOGGLE
  // -------------------------------------------------
  $( ".ul-toggle li" ).click(function() {
    $(this).toggleClass('active').find("ul").toggle( "slow");

  });
  
  // BOOTSTRAP TOGGLE
  // -------------------------------------------------
  $("[data-keep-open=true]").click(function(e) {
      e.stopPropagation();
  });
  
  // BOOTSTRAP MODAL
  // -------------------------------------------------
  $("[data-call=bs-modal]").each(function(e) {
    
    var dataOptions = $(this).attr("data-options");
    
    if(dataOptions) {
      var opts = jsonify(dataOptions);
      $(this).modal(opts);
    }
  });
  
});

// PRODUCT TOGGLE
// -------------------------------------------------
function changeView(view) {
  switch (view) {
    case "grid":
    $('.product-grid').removeClass('product-listview');
    $('.product-grid > div').removeClass('reset-col');
    break;
    case "list":
    $('.product-grid').addClass('product-listview');
    $('.product-grid > div').addClass('reset-col');
    break;
  }
}

