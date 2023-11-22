#!/usr/bin/node
const computeFactorial = (n) => {
  if (isNaN(n) || !Number.isInteger(Number(n))) {
    return 1;
  } else if (n < 0) {
    return Infinity;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
};

const inputNumber = process.argv[2];
const result = computeFactorial(inputNumber);
console.log(result);
