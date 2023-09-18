#!/usr/bin/node
const array = require('./100-data').list;
let i = 0;
function arr_mul (element) {
  return element * i++;
}
const nlist = array.map((element) => element * i++);

console.log(array);
console.log(nlist);
