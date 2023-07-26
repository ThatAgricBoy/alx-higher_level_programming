#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const tasksCompleted = {};

  if (!Array.isArray(body)) {
    console.error('Invalid response format. Expected an array.');
    return;
  }

  body.forEach((todo) => {
    // Ensure that each todo item has the required properties (userId and completed)
    if (typeof todo.userId === 'number' && typeof todo.completed === 'boolean') {
      const userId = todo.userId.toString(); // Convert to string for consistency

      // Initialize the tasksCompleted count for the current user
      if (!tasksCompleted[userId]) {
        tasksCompleted[userId] = 0;
      }

      // Increment the completed task count for the current user
      if (todo.completed) {
        tasksCompleted[userId]++;
      }
    } else {
      console.error('Invalid todo item format. Skipping:', todo);
    }
  });

  console.log(tasksCompleted);
});
