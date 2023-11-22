#!/usr/bin/node
const [arg1 = undefined] = process.argv.slice(2);

const x = parseInt(arg1);

if (!isNaN(x) && x > 0) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
