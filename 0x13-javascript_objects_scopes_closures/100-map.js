#!/usr/bin/node
const list = require('./100-data').list;

const result = list.map((x, index) => {
  return x * index;
});

console.log(list);
console.log(result);

/**
 * const array = require('./100-data').list;
let i = 0;
const nlist = array.map((element) => element * i++);

console.log(array);
console.log(nlist);
 */
