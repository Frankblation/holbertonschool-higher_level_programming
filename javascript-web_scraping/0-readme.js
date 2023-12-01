#!/usr/bin/node

const fs = require('fs');


if (process.argv.length !== 3) {
  console.error('Usage: node script.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];

try {
  const data = fs.readFileSync(filePath, 'utf-8');
  console.log(data);
} catch (err) {

  console.error(err);
}
