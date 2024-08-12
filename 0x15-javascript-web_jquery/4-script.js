#!/usr/bin/env node

// This script toggles the class of the <header> element between 'red' and 'green' when the user clicks on the <div id="toggle_header"> element

$(document).ready(() => {
  $('#toggle_header').click(() => {
    const header = $('header');
    if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    } else if (header.hasClass('green')) {
      header.removeClass('green').addClass('red');
    }
  });
});

