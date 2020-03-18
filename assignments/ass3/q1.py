import cs3311

conn = cs3311.connect()
cur1 = conn.cursor()

# TODO

q1_helper = """
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
"""

q1 = """
    SELECT code, quota, enrols
    FROM q1_helper
    WHERE enrols > quota
    ;
"""

cur1.execute(q1_helper)
cur1.execute(q1)

for record in cur1.fetchall():
    percent = round((record[2]/record[1])*100)
    print(record[0], str(percent)+"%")

cur1.close()
conn.close()
