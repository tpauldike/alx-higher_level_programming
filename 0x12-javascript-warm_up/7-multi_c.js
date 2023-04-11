#!/usr/bin/node
const n = process.argv[2];
if (parseInt(n)) {
  for (let x = 0; x < n; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
