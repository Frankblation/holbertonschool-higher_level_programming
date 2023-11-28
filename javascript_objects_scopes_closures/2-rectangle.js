#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (!Number.isInteger(w) || !Number.isInteger(h) || w <= 0 || h <= 0) {
            // If w or h is not a positive integer, create an empty object
            this.width = 0;
            this.height = 0;
        } else {
            // Initialize the instance attributes width and height
            this.width = w;
            this.height = h;
        }
    }
}