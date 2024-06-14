#!/usr/bin/node
/**
 * script that prints the title of a Star Wars movie,
 * where the episode number matches a given integer.
 * The first argument is the movie ID
 * the Star wars API with the endpoint:
 *  https://swapi-api.alx-tools.com/api/films/:id
 */
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
