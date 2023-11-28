#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
      if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
        // Throw an error if conditions are not met
        throw new Error("Invalid arguments. Width and height must be positive numbers.");
      }

      // Initialize instance attributes
      this.width = w;
      this.height = h;
    }
  }

  module.exports = Rectangle;