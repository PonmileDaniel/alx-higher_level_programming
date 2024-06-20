#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  }
  return n * factorial(n - 1);
}
const number = process.argv[2];
const no = parseInt(number);
console.log(factorial(no));
