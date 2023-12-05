#!/usr/bin/node

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      $.each(data.results, function (index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function (error) {
      console.error('Error fetching movie data:', error);
    }
  });
});
