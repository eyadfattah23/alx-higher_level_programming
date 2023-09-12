#!/usr/bin/node
let i = 0;
process.argv.forEach((val, index) => {
  i += 1;
});
const number = process.argv[2];
if (i < 3 || !(parseInt(number))) {
  console.log('Missing size');
} else {
  for (let index = 0; index < process.argv[2]; index++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
