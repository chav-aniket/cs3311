-- COMP3311 12s1 Exam Q3
-- The Q3 view must have attributes called (team,players)

drop view if exists q3Helper;
create view q3Helper
as
SELECT t.country, p.id, p.memberOf
FROM Players p INNER JOIN Teams t
ON t.id = p.memberOf
GROUP BY p.id
EXCEPT
SELECT DISTINCT t.country, p.id, p.memberOf
FROM Players p INNER JOIN Teams t ON t.id = p.memberOf, Goals g
WHERE p.id = g.scoredBy
;

drop view if exists Q3;
create view Q3
as
SELECT country, MAX(result)
FROM (SELECT country, COUNT(id) AS result
    FROM q3Helper
    GROUP BY country)
;