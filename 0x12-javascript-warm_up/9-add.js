#!/usr/bin/node
let n = 0;
process.argv.forEach((val, index) => {
  n += 1;
});
function add (n, m) {
  return n + m;
}
const a1 = parseInt(process.argv[2]);
const a2 = parseInt(process.argv[3]);

console.log(add(a1, a2));
