#!/usr/bin/node
/**
 * script that prints all characters of a Star Wars movie
 *
    The first argument is the Movie ID
    Display one character name by line
    use the Star wars API
    use the module request

 */
const request = require('request');
const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    for (const character of characters) {
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
