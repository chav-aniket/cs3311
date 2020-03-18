-- COMP3311 12s1 Exam Q4
-- The Q4 view must have attributes called (team1,team2,matches)

drop view if exists q4Helper;
create view q4Helper
as
SELECT i.match, t1.country AS A, t2.country AS B
FROM Involves i 
INNER JOIN Involves j ON i.match = j.match
INNER JOIN Teams t1 ON i.team = t1.id
INNER JOIN Teams t2 ON j.team = t2.id
WHERE i.team != j.team
GROUP BY j.match
ORDER BY t1.country, t2.country, i.match
;

drop view if exists Q4;
create view Q4
as
SELECT A, B, matches
FROM (SELECT A, B, COUNT(match) as matches
    FROM q4Helper
    GROUP BY A, B)
WHERE matches = (SELECT COUNT(match) as matches
                    FROM q4Helper
                    GROUP BY A, B
                    ORDER BY matches DESC
                    LIMIT 1)
;