-- listing info in a database
SELECT id, name FROM cities, WHERE cities.id IN (SELECT id FROM states WHERE name = California) ORDER BY id ASC;
