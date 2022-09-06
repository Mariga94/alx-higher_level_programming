#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let c = 0; c < this.height; c++) {
      let rectangle = '';
      for (let r = 0; r < this.width; r++) {
        rectangle += 'X';
      }
      console.log(rectangle);
    }
  }
}
module.exports = Rectangle;
