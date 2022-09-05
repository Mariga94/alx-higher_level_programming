#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;

function factorial (num) {
  if (num < 0) {
    console.log(-1);
  } else if (num === 0) {
    return 1;
  } else if (isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

if (len === 2) {
  console.log(1);
} else if (len === 3) {
  console.log(factorial(parseInt(argv[2])));
}
