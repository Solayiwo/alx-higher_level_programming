#!/usr/bin/node
const firstArg = process.argv[2];
const inputNum = parseInt(firstArg);

if (isNaN(inputNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + inputNum);
}
