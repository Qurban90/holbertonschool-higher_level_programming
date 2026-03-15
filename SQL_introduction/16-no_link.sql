-- Lists all records of the table second_table where name is not NULL.
-- Results display score and name, ordered by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
