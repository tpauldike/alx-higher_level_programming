#!/usr/bin/node
const n = process.argv[2];
let y = 0;
if (parseInt(n)) {
  for (let x = 0; x < n; x++) {
    console.log('X');
    while (y < n) {
      console.log('X');
      y++;
    }
  }
} else {
  console.log('Missing size');
}
