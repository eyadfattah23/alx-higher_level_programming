#!/usr/bin/node
/**
 * script that prints all characters of a Star Wars movie
 *
    The first argument is the Movie ID
    Display one character name by line
    use the Star wars API
    use the module request

 */
const request = require('request-promise-native');
const movieId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

async function printCharacters () {
  try {
    const body = await request(url);
    const characters = JSON.parse(body).characters;

    for (const character of characters) {
      const characterBody = await request(character);
      console.log(JSON.parse(characterBody).name);
    }
  } catch (error) {
    console.log(error);
  }
}

printCharacters();
