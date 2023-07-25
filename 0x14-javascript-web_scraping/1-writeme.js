#!/usr/bin/node
// script that writes a string to a file.

const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Content written to ${filePath} successfully.`);
  }
});
