#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let zähler = 0;
  list.forEach(Element => {
    if (searchElement === Element) {
      zähler += 1;
    }
  });
  return zähler;
};
