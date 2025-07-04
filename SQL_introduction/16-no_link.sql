-- Select score and name where name is not null, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
