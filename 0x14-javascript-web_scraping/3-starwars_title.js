#!/usr/bin/node

const request = require('request');
const episodeId = process.argv[2];
const BASE_API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(BASE_API_URL + episodeId, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const filmData = JSON.parse(body);
    console.log(filmData.title);
  } else {
    console.error('Error code:', response.statusCode);
  }
});
