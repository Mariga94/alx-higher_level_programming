const $ = window.$;
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    $('DIV#red_header').toggleClass('green red');
  });
});
