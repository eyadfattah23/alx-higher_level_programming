-- Active: 1694358571864@@127.0.0.1@3306@hbtn_0d_tvshows_rate
-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
LEFT JOIN tv_show_ratings
ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;


--SELECT tv_shows.title AS title, SUM(tv_show_ratings.rate) AS rate  FROM tv_show_ratings  JOIN tv_shows ON tv_shows.id = tv_show_ratings.show_id GROUP BY title ORDER BY rate DESC;
