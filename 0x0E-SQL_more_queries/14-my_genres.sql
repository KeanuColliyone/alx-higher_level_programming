-- Lists all genres of the show Dexter from the hbtn_0d_tvshows database
-- Results are sorted in ascending order by the genre name
SELECT genres.name
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;
