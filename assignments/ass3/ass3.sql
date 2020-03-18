-- COMP3311 Ass3.sql
-- Written by z5265106

-- Q1

CREATE OR REPLACE VIEW q1_helper AS
SELECT s.code AS code, 
        c.quota AS quota, 
        COUNT(DISTINCT ce.person_id) AS enrols
FROM courses c
INNER JOIN course_enrolments ce ON c.id = ce.course_id
INNER JOIN subjects s ON c.subject_id = s.id
WHERE c.quota > 50 AND c.term_id = 5199
GROUP BY c.id, c.quota, s.code
ORDER BY s.code ASC
;

-- Q2

CREATE OR REPLACE VIEW q2_helper1 AS
SELECT SUBSTRING(s.code, 1, 4) AS stream, 
        SUBSTRING(s.code, 5, 4) AS code
FROM subjects s
ORDER BY code ASC, stream ASC
;

CREATE OR REPLACE VIEW q2_helper2 AS
SELECT code, COUNT(DISTINCT stream) as codenum
FROM q2_helper1
GROUP BY code
;

-- Q3

CREATE OR REPLACE VIEW q3_helper AS
SELECT SUBSTRING(s.code, 1, 4) as stream, 
        s.code as code, 
        b.name as building
FROM subjects s
INNER JOIN courses co ON s.id = co.subject_id
INNER JOIN classes cl ON co.id = cl.course_id
INNER JOIN meetings m ON cl.id = m.class_id
INNER JOIN rooms r ON m.room_id = r.id
INNER JOIN buildings b ON r.within = b.id
WHERE co.term_id = 5196
GROUP BY stream, s.code, building
ORDER BY building ASC, stream ASC, code ASC
;

-- Q4

CREATE OR REPLACE VIEW q4_helper AS
SELECT SUBSTRING(s.code, 1, 4) as stream, 
        t.name as term,
        s.code as code, 
        COUNT(DISTINCT ce.person_id) as enrols
FROM subjects s
INNER JOIN courses c ON s.id = c.subject_id
INNER JOIN terms t ON c.term_id = t.id
INNER JOIN course_enrolments ce ON c.id = ce.course_id
GROUP BY stream, code, term
ORDER BY term ASC
;