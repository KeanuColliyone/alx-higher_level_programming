#!/usr/bin/node

function findSecondBiggest (args) {
  if (args.length < 2) {
    return 0;
  }
  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  return secondLargest;
}

const numbers = process.argv.slice(2);
console.log(findSecondBiggest(numbers));
