// JavaScript script that Uses jQuery API to fetches from the url and
// displays the value of hello from that fetch in the HTML tag DIV#hello

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data) {
  const helloTranslation = data.hello;
  $('#hello').text(helloTranslation);
});
