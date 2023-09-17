#!/usr/bin/node
const array = require('./100-data').list;
var i = 0;
function arr_mul(params) {

}
const nlist = array.map((element) => element * array.indexOf(element));

console.log(array);
console.log(nlist);
