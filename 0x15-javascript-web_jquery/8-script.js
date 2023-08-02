(function ($) {
  'use strict';

  $(document).ready(function () {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
      const movies = data.results;
      const ulElement = $('#list_movies');

      movies.forEach(function (movie) {
        const liElement = $('<li></li>').text(movie.title);
        ulElement.append(liElement);
      });
    });
  });

})(jQuery);
