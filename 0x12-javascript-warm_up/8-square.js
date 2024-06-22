#!/usr/bin/node

const arg = process.argv[2];

if (arg === undefined || isNaN(arg)) {
  console.log('Missing size');
} else {
  const size = Number(arg);
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
