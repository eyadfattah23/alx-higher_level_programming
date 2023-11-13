#!/usr/bin/node
let len = 0;
process.argv.forEach((val, index) => {
  len += 1;
});
if (len === 2) {
  console.log('No argument');
} else {
  for (let i = 2; i < len; i++) {
    console.log(process.argv[i]);
  }
}
