#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccu = 0;
  for (let a = 0; a < list.length; a++) {
    if (searchElement === list[a]) {
      nOccu++;
    }
  }
  return nOccu;
};
