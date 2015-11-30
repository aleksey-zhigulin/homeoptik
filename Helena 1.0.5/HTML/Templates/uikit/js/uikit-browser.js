// Init
// ----------------------------------------------
var srcDir = "";
var urlParams = {};
var $ajaxViewer;
var $iframeViewer;
var $errorEl = $(".ukb-error");
var $preloaderEl = $(".ukb-preloader");
var hideClass= "hidden";
var htmlMap = {"&": "&amp;","<": "&lt;",">": "&gt;",'"': '&quot;',"'": '&#39;',"/": '&#x2F;'};

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

      
// Functions
// ----------------------------------------------
function getUrlParams(url) {
  var str  = url.split("?")[1];
  var search = /([^&=]+)=?([^&]*)/g;
  var match;
  var params = {};
  
  while(match = search.exec(str)) {
    params[match[1]] = match[2];
  }
  return params;    
}

function loadPage(args) {
  $iframeViewer.hide();
  $ajaxViewer.hide();
  $errorEl.hide();
  $preloaderEl.show();
  
  switch(args.params["viewer"]) {
    case "ajax":
      $.ajax({
        crossOrigin: true,
        url: args.url,
        dataType: "html",
        success: function(data) {
          $preloaderEl.fadeOut();
          $ajaxViewer.show();
          $ajaxViewer.html(data);
          applyFunctions();
        },
        error: function(err) {
          $preloaderEl.fadeOut();
          $errorEl.fadeIn();
        }
      });
    break;
    case "iframe":
      $preloaderEl.hide();
      if(args.params["h"]) {
        $iframeViewer.height(args.params["h"]);
      }
      $iframeViewer.attr("src", args.url);
      $iframeViewer.show();
    break;
  }
}
  
function displayCode(rawCode) {
  var rgx = new RegExp("<(.*) class=\"dont-copy\">(.)*</(.)*>");
  code = rawCode.replace(rgx, "");
  var code = escapeHtml(code);
  
  $(".modal-code").modal("toggle");
  $(".modal-code pre code").html(code);
  $(".modal-code pre code").each(function(i, block) {
    hljs.highlightBlock(block);
  });
}
  
function applyFunctions() {

  var title = "Helena Ui Kit: " + $(".demo-header h1").html();
  $("title").html(title);
  
  $(".code-sample").each(function() {
    var rawHtml = $(this).find(".tab-output").html();
    var cleanHtml = escapeHtml(rawHtml);
    $(this).find(".tab-html code").html(cleanHtml);
  });
  
  $(".format-code").each(function() {
    var cleanHtml = escapeHtml($(this).html());
    $(this).html(cleanHtml);
  });
  
  $('pre code').each(function(i, block) {
    hljs.highlightBlock(block);
  });
  
  $(".copy-code").each(function() {
    $(this).click(function(e) {
        e.preventDefault();
        var code = $(this).parent().parent().html();
        displayCode(code);
    });
  });
  
  // bxslider
  callBxSlider();
  
  // jqueryUI
  callJUI();
  
  // PrettyPhoto
  $("a[data-gal^='prettyPhoto']").prettyPhoto({hook:'data-gal'});
  
  $(".load-page").click(function (e) {
    var pArgs = {};
    pArgs.url = srcDir + $(this).attr("href").replace("#", "");
    pArgs.params = getUrlParams(pArgs.url);
    loadPage(pArgs);
  });
   
}

// Doc ready
// ----------------------------------------------
$().ready(function () {
      
    // set viewers
    $ajaxViewer = $(".ajax-viewer");
    $iframeViewer = $(".iframe-viewer");
  
    // Try getting args on page load
    var pageArgs = {};
    pageArgs.url = window.location.hash.replace("#", "");
    pageArgs.params = getUrlParams(pageArgs.url);

    if(pageArgs.url) {
      loadPage(pageArgs);
    } else {
      $ajaxViewer.show(); // show default content
    }
    
    // Handle clicks
    $('[data-viewer]').click(function(e) {
      $(".ukb-nav-side .navbar-nav > li").removeClass("active");
      $(this).parent().parent().parent().addClass("active");
      pageArgs.url = srcDir + $(this).attr("href").replace("#", "");
      pageArgs.params = getUrlParams(pageArgs.url);

      loadPage(pageArgs);
     });
     
    $('.kit-demo-link').click(function(e) {
      pageArgs.url = srcDir + $(this).attr("href").replace("#", "");
      pageArgs.params = getUrlParams(pageArgs.url);

      loadPage(pageArgs);
     });
     
    // Code sample code 
    $(document).on('click', '.code-sample .cs-nav li', function (e) {
      e.preventDefault();
      $(this).siblings().removeClass("active");
      $(this).addClass("active");
      var target = $(this).children("a").attr("data-tab");
      var $parent = $(this).parent().parent();
      $parent.find(".tab").removeClass("active");
      $parent.find(target).addClass("active");
    });    
});
      