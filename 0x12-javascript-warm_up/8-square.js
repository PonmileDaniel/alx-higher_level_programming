#!/usr/bin/node
const number = parseInt(process.argv[2]);
let s;
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    s = '';
    for (let j = 0; j < number; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
