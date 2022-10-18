#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const todos = JSON.parse(body);
  const completed = {};
  todos.forEach(todo => {
    if (todo.completed) {
      if (Object.prototype.hasOwnProperty.call(completed, todo.userId)) {
        completed[todo.userId] += 1;
      } else {
        completed[todo.userId] = 1;
      }
    }
  });
  console.log(completed);
});
