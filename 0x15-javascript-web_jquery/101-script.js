#!/usr/bin/env node

// This script manages adding, removing, and clearing list items in a <ul class="my_list">

$(document).ready(() => {
  $('#add_item').click(() => {
    $('<li>Item</li>').appendTo('.my_list');
  });

  $('#remove_item').click(() => {
    $('.my_list li:last').remove();
  });

  $('#clear_list').click(() => {
    $('.my_list').empty();
  });
});

