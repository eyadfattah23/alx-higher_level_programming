#!/usr/bin/node

const NSquare = require('./5-square');
class Square extends NSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
