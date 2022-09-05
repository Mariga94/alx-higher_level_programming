#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;

function add (a, b) {
  return a + b;
}

if (len === 4) {
  console.log(add(parseInt(argv[2]), parseInt(argv[3])));
} else if (len === 3) {
  console.log('NaN');
} else if (len === 2) {
  console.log('NaN');
}
