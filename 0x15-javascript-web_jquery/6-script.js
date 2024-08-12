#!/usr/bin/env node

// This script updates the text of the <header> element to "New Header!!!" when the user clicks on the <div id="update_header"> element

$(document).ready(() => {
  $('#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});

