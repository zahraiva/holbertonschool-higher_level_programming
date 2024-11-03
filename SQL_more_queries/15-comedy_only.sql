-- sql task
SELECT tv_shows.title AS title
FROM tv_genres
INNER JOIN tv_shows.genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.show_id = tv_show_genres.show_id
WHERE tv_shows.name = 'Comedy'
ORDER BY tv_shows.title
