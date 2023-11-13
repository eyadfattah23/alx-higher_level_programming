#!/usr/bin/node

if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(process.argv[2]);
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
}
