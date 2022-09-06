#!/usr/bin/node
const count = process.argv.length;

if (count === 3) {
  console.log(`${process.argv[2]}` + ' is undefined');
} else if (count === 4) {
  console.log(`${process.argv[2]}` + ' is ' + `${process.argv[3]}`);
} else if (count === 2) {
  console.log('undefined is undefined');
}
