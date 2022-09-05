#!/usr/bin/node
const { argv } = require('node:process');
const len = argv.length;

if (len === 2) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else if (len >= 4) {
  const arr = [];
  for (let i = 0; i < len; i++) {
    if (Number.isInteger(parseInt(argv[i]))) {
      arr.push(parseInt(argv[i]));
    }
  }
  const sortDesc = arr.sort((a, b) => b - a);
  console.log(sortDesc[1]);
}
