#!/usr/bin/node
const { argv } = require('node:process');
const length = argv.length;
if (length >= 3) {
  const counter = parseInt(argv[2]);
  for (let i = 0; i < counter; i++) {
    console.log('c is fun');
  }
} else if (length === 2) {
  console.log('Missing number of occurences');
} else {
  console.log();
}
