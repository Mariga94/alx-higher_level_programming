#!/usr/bin/node
const len = process.argv.length;

function add (a, b) {
  return a + b;
}

if (len === 4) {
  console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
} else if (len === 3) {
  console.log('NaN');
} else if (len === 2) {
  console.log('NaN');
}
