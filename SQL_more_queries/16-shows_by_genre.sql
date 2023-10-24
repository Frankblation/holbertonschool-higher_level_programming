-- script that lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
SELECT genres.name FROM tv_genres AS genres
JOIN tv_show_genres AS show_genres ON show_genres.genre_id = genres.id
JOIN tv_shows AS shows ON shows.id = show_genres.show_id
WHERE shows.title='Dexter'
ORDER BY genres.name ASC;