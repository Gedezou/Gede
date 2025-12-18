SELECT name
FROM people
JOIN stars
ON stars.person_id = people.id
JOIN movies
ON movies.id = stars.movie_id
WHERE movies.title = "Toy Story";

-- SELECT COUNT(name)
-- FROM people
-- WHERE person_id =
-- (
--     SELECT id
--     FROM movies
--     WHERE title = 'Toy Story'
-- --

-- )