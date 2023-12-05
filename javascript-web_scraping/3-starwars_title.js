#!/usr/bin/node

const request = require('request');

// Function to get the title of a Star Wars movie based on the episode number
function getStarWarsMovieTitle (movieID) {
  const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieID}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Status Code:', response.statusCode);
    } else {
      try {
        const movieData = JSON.parse(body);
        console.log(`${movieData.title}`);
      } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
      }
    }
  });
}

const args = process.argv.slice(2);
const movieID = parseInt(args[0]);

if (isNaN(movieID) || movieID <= 0) {
  console.error('Please provide a valid positive integer as the movie ID.');
} else {

  getStarWarsMovieTitle(movieID);
}
