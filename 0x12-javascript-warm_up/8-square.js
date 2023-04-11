#!/usr/bin/node
const n = process.argv[2];
let y = 0;
let square = '';
if (parseInt(n)) {
  for (let x = 0; x < n; x++) {
    while (y < n) {
      square += 'X';
      y++;
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
