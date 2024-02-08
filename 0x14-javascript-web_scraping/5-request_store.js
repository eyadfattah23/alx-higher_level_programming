#!/usr/bin/node
const fs = require('fs');
const request = require('request');
/* request.get(process.argv[2], (error, body) => {
    if (error) console.log(error);
    else {
        fs.writeFile(process.argv[3], body, 'utf8', (error) => {
            if (error) console.log(error);
        });
    }
});
*/

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
