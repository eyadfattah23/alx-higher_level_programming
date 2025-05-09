-- script that lists all genres and displays the number of shows linked to each.

SELECT tv_genres.name AS genre, COUNT(show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;


-- SELECT tv_genres.name as genre, COUNT(tv_show_genres.show_id) as number_of_shows
-- FROM tv_show_genres
-- JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
-- GROUP BY genre;
