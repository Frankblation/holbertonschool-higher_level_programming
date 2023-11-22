#!/opt/homebrew/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const [arg = NaN] = process.argv.slice(2);

const num = parseInt(arg);

const result = factorial(num);

console.log(result);
