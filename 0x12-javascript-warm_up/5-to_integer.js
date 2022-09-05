#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length >= 3) {
  const int = parseInt(argv[2]);

  if (Number.isInteger(int)) {
    console.log('My number: ' + int);
  } else {
    console.log(`${argv[2]}` + ' Not a number');
  }
} else {
  console.log('Not a number');
}
