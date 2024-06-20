#!/usr/bin/node
const argvCount = process.argv[2];

if (argvCount) {
  console.log(argvCount);
} else {
  console.log('No argument');
}
