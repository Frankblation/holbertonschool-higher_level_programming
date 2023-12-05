#!/usr/bin/node
const request = require('request');

// Function to compute the number of tasks completed by each user
function completedTasksByUser (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      try {
        const todos = JSON.parse(body);

        // Create a map to store the count of completed tasks for each user
        const completedTasksCount = {};

        // Iterate through the todos and count completed tasks for each user
        todos.forEach((todo) => {
          if (todo.completed) {
            if (completedTasksCount[todo.userId]) {
              completedTasksCount[todo.userId]++;
            } else {
              completedTasksCount[todo.userId] = 1;
            }
          }
        });

        console.log(completedTasksCount);
      } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
      }
    } else {
      console.error('Error:', error);
    }
  });
}

// Get API URL from command line arguments
const args = process.argv.slice(2);
const apiUrl = args[0];

// Check if the provided API URL is valid
if (apiUrl) {
  completedTasksByUser(apiUrl);
} else {
  console.error('Please provide the API URL as the first argument.');
}
