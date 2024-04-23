#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => {
    return count + (current === searchElement ? 1 : 0);
  }, 0);
};
