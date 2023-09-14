#!/usr/bin/node
const array = require('./100-data').list;

const nlist = array.map((element) => element * array.indexOf(element));

console.log(array);
console.log(nlist);
