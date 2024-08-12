#!/usr/bin/env node

// This script changes the text color of the <header> element to red when the user clicks on the <div id="red_header"> element

$(document).ready(() => {
  $('#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
