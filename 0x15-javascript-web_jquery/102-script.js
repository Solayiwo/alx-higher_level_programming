// JavaScript script that fetches and prints how to say “Hello”
// depending on the language from an API service using JQuery API

$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;
    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
