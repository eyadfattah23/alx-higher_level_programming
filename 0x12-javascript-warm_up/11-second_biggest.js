#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
}
const array = process.argv;

array.sort();

console.log(array[array.length - 2]);
