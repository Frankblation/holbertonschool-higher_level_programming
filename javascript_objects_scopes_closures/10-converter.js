#!/usr/bin/node

exports.converter = function (base) {
  this.toString = function (number) {
    return number.toString(base);
  };
};
