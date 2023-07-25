#!/usr/bin/node
// script to write to a file

const fs = require('fs');

// Get the file path and the string to write from command-line arguments
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the content to the file using utf-8 encoding
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    // If an error occurred during writing, print the error object
    console.error(err);
  } else {
    console.log(`Content written to ${filePath} successfully.`);
  }
});
