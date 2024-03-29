-- Lists all shows from the hbtn_0d_tvshows database that do not have a genre linked
-- Displays each show's title and genre_id (which will be NULL)
-- Sorts the results in ascending order by tv_shows.title
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
