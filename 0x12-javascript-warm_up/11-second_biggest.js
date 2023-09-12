#!/usr/bin/node
if (process.argv.length < 4) {
	console.log(0);
}
const array = process.argv;
for (let index = 0; index < array.length; index++) {
	parseInt(array[index]);

}
array.sort();

console.log(array[array.length - 2]);
