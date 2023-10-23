-- Active: 1694358571864@@127.0.0.1@3306@hbtn_0d_tvshows_rate
-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
