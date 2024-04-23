#!/usr/bin/node
'use strict';

const fs = require('fs');
const process = require('process');

const [fileA, fileB, fileC] = process.argv.slice(2);

if (!fileA || !fileB || !fileC) {
  console.error('Usage: ./102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

function concatFiles (source1, source2, destination) {
  fs.readFile(source1, 'utf8', (err, data1) => {
    if (err) {
      console.error(`Error reading ${source1}: ${err}`);
      return;
    }

    fs.readFile(source2, 'utf8', (err, data2) => {
      if (err) {
        console.error(`Error reading ${source2}: ${err}`);
        return;
      }

      const combinedData = `${data1}\n${data2}`;

      fs.writeFile(destination, combinedData, (err) => {
        if (err) {
          console.error(`Error writing to ${destination}: ${err}`);
        } else {
          console.log(`Files ${source1} and ${source2} were concatenated into ${destination}`);
        }
      });
    });
  });
}

concatFiles(fileA, fileB, fileC);
