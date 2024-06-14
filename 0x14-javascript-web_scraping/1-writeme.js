#!/usr/bin/node
const fs = require('fs');

const content = process.argv[3];

try {
  fs.writeFileSync(process.argv[2], content);
  // file written successfully
} catch (err) {
  console.error(err);
}
