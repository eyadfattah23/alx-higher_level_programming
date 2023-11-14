#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let index = 0; index < 3; index++) {
    theFunction();
  }
};
