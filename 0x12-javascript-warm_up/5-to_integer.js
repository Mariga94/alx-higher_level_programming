#!/usr/bin/node
const count = process.argv.length;

if (count >= 3) {
  const int = parseInt(process.argv[2]);

  if (Number.isInteger(int)) {
    console.log('My number: ' + int);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
