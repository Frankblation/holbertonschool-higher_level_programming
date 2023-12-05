#!/usr/bin/node
const request = require('request');

// Function to get the number of movies where "Wedge Antilles" is present
function getMoviesWithWedgeAntilles (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Status Code:', response.statusCode);
    } else {
      try {
        const filmsData = JSON.parse(body).results;
        let count = 0;

        filmsData.forEach((film) => {
          if (film.characters.some((character) => character.includes('/18/'))) {
            count++;
          }
        });

        console.log(count);
      } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
      }
    }
  });
}

// Get API URL from command line arguments
const args = process.argv.slice(2);
const apiUrl = args[0];

// Check if the provided API URL is valid
if (!apiUrl) {
  console.error('Please provide the API URL as the first argument.');
} else {
  // Fetch and print the number of movies with Wedge Antilles
  getMoviesWithWedgeAntilles(apiUrl);
}
