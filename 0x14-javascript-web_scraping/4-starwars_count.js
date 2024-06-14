#!/usr/bin/node
/**
 * script that prints number of movies where,
 * the character “Wedge Antilles” is present.
 * The first argument is https://swapi-api.alx-tools.com/api/films/
 * Wedge Antilles is character ID 18
 * the Star wars API with the endpoint:
 *  https://swapi-api.alx-tools.com/api/films/
 */
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(body.split('/people/18/').length - 1);
  }
});
