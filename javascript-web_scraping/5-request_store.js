#!/usr/bin/node
const request = require('request');
const fs = require('fs');

function saveWebpage (url, filePath) {
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf-8', (writeError) => {
        // File written without errors
      });
    }
  });
}

const args = process.argv.slice(2);
const url = args[0];
const filePath = args[1];

if (url && filePath) {
  saveWebpage(url, filePath);
} else {
  console.error('Please provide both a URL and a file path.');
}
