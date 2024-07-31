#!/usr/bin/node
const request = require('request');
const ids = process.argv[2];
request('http://swapi.co/api/films/' + ids + '/', function (error, response, body) {
  if (error == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
