-- Lists all shows and their linked genres from the hbtn_0d_tvshows database
-- Shows without a genre will display NULL in the genre column
-- Results are sorted in ascending order by show title and genre name
SELECT tv_shows.title, genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN genres ON tv_show_genres.genre_id = genres.id
ORDER BY tv_shows.title ASC, genres.name ASC;
