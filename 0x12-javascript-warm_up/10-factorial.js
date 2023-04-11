#!/usr/bin/node
function factr (n) {
  return n === 0 || isNaN(n) ? 1 : n * factr(n - 1);
}
const arg1 = parseInt(process.argv[2]);
console.log(factr(arg1));
