-- COMP3311 19T3 Assignment 2
-- Written by Aniket Chavan

-- Q1 Which movies are more than 6 hours long? 

create or replace view Q1(title)
as
SELECT main_title AS title
FROM titles
WHERE runtime > 360 AND titles.format = 'movie'
;


-- Q2 What different formats are there in Titles, and how many of each?

create or replace view Q2(format, ntitles)
as
SELECT DISTINCT format, COUNT(titles) AS ntitles
FROM titles
GROUP BY titles.format
;


-- Q3 What are the top 10 movies that received more than 1000 votes?

create or replace view Q3(title, rating, nvotes)
as
SELECT main_title, rating, nvotes
FROM titles
WHERE format = 'movie' and nvotes > 1000
ORDER BY rating DESC, main_title ASC
limit 10
;


-- Q4 Helper View

CREATE OR REPLACE VIEW Q4_helper(title, rating, nepisodes)
AS
SELECT t.main_title AS title,
		t.rating,
		COUNT(e.episode) AS nepisodes
FROM titles t 
INNER JOIN episodes e ON t.id = e.parent_id
WHERE t.format = 'tvSeries' OR t.format = 'tvMiniSeries'
GROUP BY title, t.rating
;


-- Q4 What are the top-rating TV series and how many episodes did each have?

create or replace view Q4(title, nepisodes)
as
SELECT title, nepisodes
FROM Q4_helper
WHERE rating = (SELECT MAX(rating) FROM Q4_helper)
;


-- Q5 Helper View
CREATE OR replace VIEW Q5_helper(title, nlanguages)
AS
SELECT t.main_title AS title, 
		COUNT(DISTINCT a.language) AS nlanguages
FROM titles t 
INNER JOIN aliases a ON t.id = a.title_id
WHERE t.format = 'movie'
GROUP BY t.id
;


-- Q5 Which movie was released in the most languages?

create or replace view Q5(title, nlanguages)
as
SELECT title, nlanguages
FROM Q5_helper
WHERE nlanguages = (SELECT MAX(nlanguages) FROM Q5_helper)
;


-- Q6 Helper View

CREATE OR REPLACE VIEW Q6_helper(name, rating)
AS
SELECT n.name, AVG(t.rating) AS rating
FROM names n
INNER JOIN known_for k ON n.id = k.name_id
INNER JOIN titles t ON k.title_id = t.id
INNER JOIN worked_as w ON n.id = w.name_id
WHERE t.rating IS NOT NULL
	AND w.work_role = 'actor'
	AND t.format = 'movie'
GROUP BY n.name
HAVING COUNT(n.name) > 1
;


-- Q6 Which actor has the highest average rating in movies that they're known for?

create or replace view Q6(name)
as
SELECT name
FROM Q6_helper
WHERE rating = (SELECT MAX(rating) FROM Q6_helper)
;


-- Q7 Helper View

CREATE OR REPLACE VIEW Q7_helper(id, genres)
AS
SELECT t.id AS id, STRING_AGG(genre, ',' ORDER BY genre ASC) as genres
FROM titles t
INNER JOIN title_genres tg ON t.id = tg.title_id
WHERE format = 'movie'
GROUP BY id
HAVING COUNT(genre) > 3
;

-- Q7 For each movie with more than 3 genres, show the movie title and a comma-separated list of the genres


create or replace view Q7(title, genres)
as
SELECT t.main_title as title, q.genres
FROM titles t
INNER JOIN Q7_helper q ON t.id = q.id
;

-- Q8 Get the names of all people who had both actor and crew roles on the same movie

create or replace view Q8(name)
as
SELECT DISTINCT n.name
FROM names n, actor_roles a, crew_roles c, titles t
WHERE n.id = a.name_id
	AND a.name_id = c.name_id
	AND a.title_id = c.title_id
	AND a.title_id = t.id
	AND t.format = 'movie'
;

-- Q9 Helper View

CREATE OR REPLACE VIEW Q9_helper(name, age)
AS
SELECT n.name, (t.start_year - n.birth_year) as age
FROM names n, titles t, actor_roles a
WHERE t.format = 'movie'
	AND n.id = a.name_id
	AND a.title_id = t.id
;

-- Q9 Who was the youngest person to have an acting role in a movie, and how old were they when the movie started?

create or replace view Q9(name, age)
as
SELECT q.name, age
FROM Q9_helper q
WHERE age = (SELECT MIN(age) FROM Q9_helper)
;

-- Q10 Write a PLpgSQL function that, given part of a title, shows the full title and the total size of the cast and crew

-- create or replace function
-- 	Q10(partial_title text) returns setof text
-- as $$

-- $$ language plpgsql;

