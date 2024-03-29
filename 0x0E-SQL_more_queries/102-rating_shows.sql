-- Lists all shows from hbtn_0d_tvshows_rate by their total rating
-- Each record displays the show title and the sum of its ratings
-- Results are sorted in descending order by the total rating
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
