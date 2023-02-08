#!/usr/bin/node
const num = process.argv[2];

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let msg = '';
    for (let j = 0; j < num; j++) {
      msg = msg + 'X';
    }
    console.log(msg);
  }
}
