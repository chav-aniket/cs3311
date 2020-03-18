-- COMP3311 12s1 Exam Q2
-- The Q2 view must have one attribute called (player,goals)

drop view if exists Q2;
create view Q2
as
SELECT p.name, COUNT(g.id) as numGoals
FROM Players p INNER JOIN Goals g
ON g.scoredBy = p.id
WHERE g.rating = "amazing"
GROUP BY p.id
HAVING (numGoals > 1)
;

-- drop view if exists Q2;
-- create view Q2
-- as
-- SELECT name, numGoals
-- FROM q2Helper
-- WHERE numGoals > 1
-- ;
