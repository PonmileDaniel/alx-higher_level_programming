#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error === null) {
    const taskCountByUser = {};
    const tasks = JSON.parse(body);
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed === true) {
        if (taskCountByUser[tasks[i].userId] === undefined) {
          taskCountByUser[tasks[i].userId] = 0;
        }
        taskCountByUser[tasks[i].userId]++;
      }
    }
    console.log(taskCountByUser);
  } else {
    console.error('Error:', error);
  }
});https://intranet.alxswe.com/#
