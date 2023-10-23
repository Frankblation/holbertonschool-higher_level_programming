-- Script to join the cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON states.id = cities.states_id
ORDER cities.id ASC;