#!/usr/bin/node
let i = 0;
let j = 0;
process.argv.forEach((val, index) => {
  i += 1;
});
const number = process.argv[2];
if (i < 3 || !(parseInt(number))) {
  console.log('Missing number of occurrences');
} else {
  while (j < process.argv[2]) {
    console.log('C is fun');
    j++;
  }
}
