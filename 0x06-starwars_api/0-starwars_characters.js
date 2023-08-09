#!/usr/bin/node
/**
 * Prints the names of characters from a specified Star Wars movie.
 * The movie's ID should be provided as the first command-line argument.
 * Each character's name is displayed on a separate line, following the order in the movie's character list.
 */

const request = require('request');
const movieId = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Initiates an API request; 'async' is used to allow 'await' for promises
request(filmURL + movieId, async (err, res, body) => {
  if (err) return console.error(err);

  // Extracts the list of character URLs from the movie's data
  const characterURLList = JSON.parse(body).characters;

  // Utilizes the character URL list to make separate requests for each character's data
  // 'await' ensures requests are queued and resolved in order
  for (const characterURL of characterURLList) {
    await new Promise((resolve, reject) => {
      request(characterURL, (err, res, body) => {
        if (err) return console.error(err);

        // Extracts and prints the name of each character in the order of their URLs
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
