#!/usr/bin/node

let i = 0;
process.argv.forEach((val, index) => {
  i += 1;
});
if (i === 2) {
  console.log('undefined is undefined');
} else if (i === 3) {
  console.log(process.argv[2] + ' is ' + 'undefined');
} else if (i === 4) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
