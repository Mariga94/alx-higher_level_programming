const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(document).ready(function () {
  $.get(url, function (data, textStatus, jqXHR) {
    $('DIV#hello').text(data.hello);
  });
});
