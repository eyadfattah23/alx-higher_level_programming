#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (process.argv.length === 2 || !num) {
  console.log('Missing size');
} else {
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      for (let j = 0; j < num; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}
/**
 *   for (let index = 0; index < process.argv[2]; index++) {
console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
 */
