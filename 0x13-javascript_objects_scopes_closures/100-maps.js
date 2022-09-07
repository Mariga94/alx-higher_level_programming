#!/usr/bin/node
const list = require('./100-data.js').list;
const map1 = list.map((val, index) => val * index);
console.log(map1);
