// JavaScript script that Uses jQuery API to fetches and lists the title for all
// movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  const films = data.results;
  for (const film of films) {
    const listItem = $('<li></li>').text(film.title);
    $('#list_movies').append(listItem);
  }
});
