#!/usr/bin/node
const { argv } = require('node:process');
const length = argv.length;

if (length >= 3) {
	let size = parseInt(argv[2]);
	if (Number.isInteger(size)) {
		let string = '';
		for (let i = 0; i < size; i++) {
			for (let j = 0; j < size; j++) {
				string += '#';
			}
			string += '\n';
		}
		console.log(string);
	} else {
		console.log('Missing size');
	}
} else if (length == 2) {
	console.log('Missing size');
} else if (length < 0) {
	console.log();
}
