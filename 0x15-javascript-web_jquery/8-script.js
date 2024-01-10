$(document).ready(function () {
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(apiUrl, function (data) {
    const listMovies = $('#list_movies');

    data.results.forEach(function (movie) {
      const title = movie.title;
      const listItem = $('<li>').text(title);
      listMovies.append(listItem);
    });
  });
});
