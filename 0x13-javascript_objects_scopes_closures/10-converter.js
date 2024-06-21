#!/usr/bin/node

exports.converter = function (base) {
  // A function that converts a number from base 10 to another base

  return function (value) {
    return value.toString(base);
  };
};
