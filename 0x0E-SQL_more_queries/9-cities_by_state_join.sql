-- Lists all cities from the hbtn_0d_usa database, displaying each city's ID, city name, and state name
-- Results are sorted in ascending order by cities.id
-- This script uses implicit join syntax to combine data from cities and states tables
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
