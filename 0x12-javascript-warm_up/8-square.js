#!/usr/bin/node
const length = process.argv.length;

if (length >= 3) {
  const size = parseInt(process.argv[2]);
  if (Number.isInteger(size)) {
    for (let i = 0; i < size; i++) {
      let string = '';
      for (let j = 0; j < size; j++) {
        string += '#';
      }
      console.log(string);
    }
  } else {
    console.log('Missing size');
  }
} else if (length === 2) {
  console.log('Missing size');
} else if (length < 0) {
	console.log();
}
