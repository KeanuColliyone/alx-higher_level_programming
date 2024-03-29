-- Lists all the cities of California found in the hbtn_0d_usa database
-- Sorts the results in ascending order by cities.id
-- Utilizes a subquery to match the state_id without using JOIN
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
