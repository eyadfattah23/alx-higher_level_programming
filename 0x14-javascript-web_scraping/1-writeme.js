#!/usr/bin/node

const fs = require('fs');
const fInput = process.argv[3];
fs.writeFile(process.argv[2], fInput, (err) => {
  if (err) throw err;
});
