#!/usr/bin/node
function factr (a) {
  if (a === 1) {
		return (a);
	}
	return (a * factr(a-1));
}

if (process.argv.length < 2) {
  console.log(factr(1));
} else {
	const arg1 = parseInt(process.argv[2]);
  console.log(factr(arg1));
}
