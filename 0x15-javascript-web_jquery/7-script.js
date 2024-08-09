// JavaScript script that Uses jQuery API to fetches the character name
// from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (data) {
  const characterName = data.name;
  $('#character').text(characterName);
});
