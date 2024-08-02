#!/usr/bin/node
const request = require('request');
let countFilmsWithCharacter18 = 0;

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const movies = data.results;
    for (let i = 0; i < movies.length; i++) {
      const characters = movies[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('/18/')) {
          countFilmsWithCharacter18++;
        }
      }
    }
  }
  console.log(countFilmsWithCharacter18);
});
