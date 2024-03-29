-- Lists all genres not linked to the show Dexter from the hbtn_0d_tvshows database
-- Results are sorted in ascending order by the genre name
SELECT genres.name
FROM genres
WHERE genres.id NOT IN (
  SELECT tv_show_genres.genre_id
  FROM tv_shows
  JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  WHERE tv_shows.title = 'Dexter'
)
ORDER BY genres.name ASC;
