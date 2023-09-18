#!/usr/bin/node
const array = require('./100-data').list;
let i = 0;
const nlist = array.map((element) => element * i++);

console.log(array);
console.log(nlist);
