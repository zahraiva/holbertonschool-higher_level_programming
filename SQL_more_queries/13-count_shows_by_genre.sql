-- listing all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genres_name AS genre COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genres_name
ORDER BY number_of_shows;