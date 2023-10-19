-- script that lists all cities contained in the database 

SELECT cities.id, cities.name, states.name
FROM cities
WHERE cities.state_id = states.id
ORDER BY citites.id;
