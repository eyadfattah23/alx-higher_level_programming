-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT name
FROM tv_show_genres, tv_genres
WHERE show_id = (SELECT id 
				FROM tv_shows
				WHERE title = 'Dexter')
	AND name = (SELECT name
				FROM tv_genres
				WHERE id = genre_id)
