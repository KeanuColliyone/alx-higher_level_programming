#!/usr/bin/env node

// This script adds the class 'red' to the <header> element when the user clicks on the <div id="red_header"> element

$(document).ready(() => {
  $('#red_header').click(() => {
    $('header').addClass('red');
  });
});

