-- Displays shows by genre
SELECT sh.title, g.genre_id FROM tv_shows AS sh
RIGHT JOIN tv_show_genres AS g
ON g.show_id = sh.id
ORDER BY sh.title, g.genre_id;