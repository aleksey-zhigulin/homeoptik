$().ready(function() {

  var path = "switcher.code";
  
  $.ajax({
  crossOrigin: true,
  url: path,
  dataType: "html",
  success: function(data) {
    $("body").append(data);
  },
  error: function(err) {
    console.log(err.statusText);        
  }
});

});