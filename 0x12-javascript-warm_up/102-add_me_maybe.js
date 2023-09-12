#!/usr/bin/node
let num;
exports.addMeMaybe = function (number, theFunction) {
  num = function (number) {
    return number + 1;
  };
  theFunction(num(number));
};
