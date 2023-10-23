-- Script that shows all cities in California in database
SELECT id, name FROM cities WHERE state_id = 1 ORDER BY cities.id;