-- Lists all genres by their total rating from the hbtn_0d_tvshows_rate database
-- Each record displays the genre name and the sum of ratings for shows within that genre
-- Results are sorted in descending order by the total rating
SELECT genres.name, SUM(tv_show_ratings.rating) AS rating
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY genres.name
ORDER BY rating DESC;
