#!/usr/bin/env node

// This script fetches the character name from the given URL and displays it in the <div id="character"> element

$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
    $('#character').text(data.name);
  });
});

