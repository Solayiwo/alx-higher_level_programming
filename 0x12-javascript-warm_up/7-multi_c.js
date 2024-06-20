#!/usr/bin/node

const firstArg = process.argv[2];
const inputNum = parseInt(firstArg);

if (isNaN(inputNum)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < inputNum; i++) {
    console.log('C is fun');
  }
}
