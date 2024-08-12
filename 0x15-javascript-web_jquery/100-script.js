#!/usr/bin/env node

// This script changes the text color of the <header> element to red

document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
});

