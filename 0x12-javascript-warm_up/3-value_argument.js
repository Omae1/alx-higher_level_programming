#!/usr/bin/node
process.argv.slice(2).for ((arg, index) => {
  console.log('${arg}');
});
