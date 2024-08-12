#!/usr/bin/env node

// This script fetches the translation of "hello" from the given URL and displays it in the <div id="hello"> element

$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    $('#hello').text(data.hello);
  });
});

