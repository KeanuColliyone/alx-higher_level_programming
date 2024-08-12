#!/usr/bin/env node

// This script fetches the titles of all movies and lists them in the <ul id="list_movies"> element

$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    const movies = data.results;
    movies.forEach(movie => {
      $('<li></li>').text(movie.title).appendTo('#list_movies');
    });
  });
});

