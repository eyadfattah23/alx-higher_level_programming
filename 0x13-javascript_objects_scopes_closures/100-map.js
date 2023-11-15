#!/usr/bin/node
const list = require('./100-data').list;

const result = list.map((x, index) => {
  return x * index;
});

console.log(list);
console.log(result);
