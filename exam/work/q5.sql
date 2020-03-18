-- COMP3311 12s1 Exam Q5
-- The Q5 view must have attributes called (team,reds,yellows)

drop view if exists Q5;
create view Q5
as
SELECT DISTINCT y.country, ifnull(r.reds, 0) AS reds, ifnull(y.yellows, 0) AS yellows
FROM 
    (SELECT t.id, t.country, COUNT(*) AS yellows, c.cardType
    FROM Cards c JOIN Players p ON c.givenTo = p.id
        JOIN Teams t ON p.memberOf = t.id
    WHERE c.cardType = 'yellow'
    GROUP BY t.country
    ) y
LEFT JOIN
    (SELECT t.id, t.country, COUNT(*) AS reds, c.cardType
    FROM Cards c JOIN Players p ON c.givenTo = p.id
        JOIN Teams t ON p.memberOf = t.id
    WHERE c.cardType = 'red'
    GROUP BY t.country
    ) r
ON r.id = y.id
;