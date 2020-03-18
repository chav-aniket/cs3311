-- COMP3311 12s1 Exam Q6
-- The Q6 view must have attributes called
-- (location,date,team1,goals1,team2,goals2)

drop view if exists q6Helper;
create view q6Helper
as
SELECT m.id as match, m.city, m.playedOn, 
    t1.country AS team1, t1.id AS id1, 
    t2.country AS team2, t2.id AS id2
FROM Matches m
INNER JOIN  Involves i ON m.id = i.match
INNER JOIN Involves j ON i.match = j.match
INNER JOIN Teams t1 ON i.team = t1.id
INNER JOIN Teams t2 ON j.team = t2.id
INNER JOIN Goals g ON m.id = g.scoredIn
WHERE i.team != j.team
GROUP BY j.match
ORDER BY t1.country, t2.country, i.match
;

drop view if exists Q6;
create view Q6
as
SELECT x.city, x.playedOn, x.team1, ifnull(x.goals1,0) AS goals1, y.team2, ifnull(y.goals2,0) AS goals2
FROM 
(SELECT q.match, q.city, q.playedOn, q.team1, q.id1, COUNT(g.id) AS goals1
    FROM q6Helper q
    JOIN Players p ON q.id1 = p.memberOf
    JOIN Goals g ON p.id = g.scoredBy
    GROUP BY q.city, q.playedOn, q.team1
) x
LEFT JOIN 
(SELECT q.match, q.city, q.playedOn, q.team2, q.id2, COUNT(g.id) AS goals2
    FROM q6Helper q
    JOIN Players p ON q.id2 = p.memberOf
    JOIN Goals g ON p.id = g.scoredBy
    GROUP BY q.city, q.playedOn, q.team2
) y
ON x.match = y.match
ORDER BY x.playedOn ASC
;