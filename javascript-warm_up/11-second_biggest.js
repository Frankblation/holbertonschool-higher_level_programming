#!/usr/bin/node

const args = process.argv.slice(2);

const numbers = args.map(arg => parseInt(arg));

const validNumbers = numbers.filter(num => !isNaN(num));

const sortedNumbers = validNumbers.sort((a, b) => b - a);

console.log(sortedNumbers.length >= 2 ? sortedNumbers[1] : 0);
