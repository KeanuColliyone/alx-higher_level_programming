-- Lists all shows from the hbtn_0d_tvshows database, including those without a genre
-- Displays each show's title and genre_id (NULL if the show has no genre)
-- Sorts the results in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
