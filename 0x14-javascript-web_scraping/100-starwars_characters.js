#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request.get(url, { json: true }, (error, response, data) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = data.characters;
  const characterNames = [];

  // Use a counter to track the number of characters processed
  let count = 0;

  // Loop through each character URL and make a request to fetch the character data
  characters.forEach((characterUrl) => {
    request.get(characterUrl, { json: true }, (error, response, characterData) => {
      if (error) {
        console.error(error);
        return;
      }

      characterNames.push(characterData.name);
      count++;

      // Check if all characters have been processed before printing the names
      if (count === characters.length) {
        console.log(characterNames.join('\n'));
      }
    });
  });
});
