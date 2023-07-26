#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasksCompleted = {};

  // Loop through each to-do item in the response array
  body.forEach((todo) => {
    const userId = todo.userId;

    // Initialize the tasksCompleted count for the current user
    if (!tasksCompleted[userId]) {
      tasksCompleted[userId] = 0;
    }

    // Increment the completed task count for the current user
    if (todo.completed) {
      tasksCompleted[userId]++;
    }
  });

  console.log(tasksCompleted);
});
