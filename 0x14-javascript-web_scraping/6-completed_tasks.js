#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasksCompleted = {};

  // Loop through each user ID (key) in the response
  for (const userId in body) {
    // Get the array of to-do items for the current user
    const todos = body[userId];

    // Initialize the tasksCompleted count for the current user
    tasksCompleted[userId] = 0;

    // Loop through each to-do item and count completed tasks for the user
    todos.forEach((todo) => {
      if (todo.completed) {
        tasksCompleted[userId]++;
      }
    });
  }

  console.log(tasksCompleted);
});
