#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.height; col++) {
        let sqr = '';
        for (let row = 0; row < this.width; row++) {
          sqr += c;
        }
        console.log(sqr);
      }
    }
  }
}
module.exports = Square;
