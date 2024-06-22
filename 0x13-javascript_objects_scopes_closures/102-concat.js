#!/usr/bin/node
const fs = require('fs');

const source1 = fs.readFileSync(process.argv[2]).toString();
const source2 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], source1 + source2);
