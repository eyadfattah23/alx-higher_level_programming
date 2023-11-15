#!/usr/bin/node
const dict = require('./101-data').dict;
const result = {};

for (const key in dict) {
  const element = dict[key];
  if (element in result) {
    result[element].push(key);
  } else {
    result[element] = [];
    result[element].push(key);
  }
}
console.log(result);

/** create
script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence. */
