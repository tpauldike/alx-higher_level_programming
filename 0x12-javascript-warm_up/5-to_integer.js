#!/usr/bin/node
if ((process.argv[2] | 0) != process.argv[2]) {
  console.log('Not a number');
} else {
  console.log('My number: ' + process.argv[2]);
}
