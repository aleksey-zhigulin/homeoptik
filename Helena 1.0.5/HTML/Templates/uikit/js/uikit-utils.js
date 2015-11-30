// UTILITY FUNCTIONS
// =============================================
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
