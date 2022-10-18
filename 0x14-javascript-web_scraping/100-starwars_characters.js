#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

request(url + movieId, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const people = JSON.parse(body).characters;
  people.forEach(actor => {
    request(actor, function (err, res, body) {
      if (!err) {
        const characters = JSON.parse(body);
        console.log(characters.name);
      }
    });
  });
});
