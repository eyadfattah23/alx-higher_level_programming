#!/usr/bin/node
let i = 0;
process.argv.forEach((val, index) => {
	i += 1;
});
let number = process.argv[2];
if (i < 3 || !(parseInt(number))) {
	console.log('Not a number');
}
else {
	console.log('My number: ' + parseInt(number));
}
