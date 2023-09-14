#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbOccurences = 0;
  for (let index = 0; index < list.length; index++) {
    if (searchElement === list[index]) {
      nbOccurences += 1;
    }
  }
  return nbOccurences;
};
