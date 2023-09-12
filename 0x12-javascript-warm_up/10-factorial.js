#!/usr/bin/node
function fact (num) {
  if (num === 1 || num === 0 || !num) {
    return 1;
  }
  return num * fact(num - 1);
}
console.log(fact(parseInt(process.argv[2])));
