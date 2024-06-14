#!/usr/bin/node
/**
 * script that computes the number of tasks completed by user id.

    The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
    Only print users with completed task
 */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const dict = {};
    for (const task of todos) {
      if (task.completed) {
        const userId = task.userId;
        if (dict[userId]) {
          dict[userId] += 1;
        } else {
          dict[userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
