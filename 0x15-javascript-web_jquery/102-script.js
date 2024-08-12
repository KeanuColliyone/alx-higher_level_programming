#!/usr/bin/env node

// This script fetches and prints how to say “Hello” depending on the language entered in the INPUT#language_code

$(document).ready(() => {
  $('#btn_translate').click(() => {
    const langCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;

    $.get(apiUrl, (data) => {
      $('#hello').text(data.hello);
    });
  });
});

