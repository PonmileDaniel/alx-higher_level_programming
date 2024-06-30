#!/usr/bin/node
let nn = 0;

exports.logMe = function (item) {
  console.log(nn + ': ' + item);
  nn++;
};
