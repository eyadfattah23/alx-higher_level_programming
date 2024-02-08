#!/usr/bin/node

const fileName = process.argv[2];

const fs = require('fs');

try {
  const data = fs.readFileSync(fileName, { encoding: 'utf8' });
  console.log(data);
} catch (error) {
  console.error(error);
}
