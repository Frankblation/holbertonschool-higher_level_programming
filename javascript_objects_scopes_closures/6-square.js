#!/usr/bin/node
const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
