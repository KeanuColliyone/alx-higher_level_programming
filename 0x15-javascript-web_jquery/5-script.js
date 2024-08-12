#!/usr/bin/env node

// This script adds a <li> element to UL.my_list when the user clicks on the <div id="add_item"> element

$(document).ready(() => {
  $('#add_item').click(() => {
    $('<li>Item</li>').appendTo('ul.my_list');
  });
});

