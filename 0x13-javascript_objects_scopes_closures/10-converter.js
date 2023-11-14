#!/usr/bin/node
exports.converter = function (base) {
  function intParser (num) {
    return num.toString(base);
  }
  return intParser;
};
