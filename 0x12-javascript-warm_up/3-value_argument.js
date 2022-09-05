#!/usr/bin/node
const { argv } = require('node:process');
const length = argv.reduce(val => val + 1, 0);
if (length <= 2) {
  console.log('No argument');
} else {
  const arr = argv.slice(2);
  arr.forEach(val => console.log(val));
}
