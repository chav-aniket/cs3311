import cs3311
import sys

conn = cs3311.connect()

cur1 = conn.cursor()

# TODO

q4_helper = """
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
"""

q4 = """
    SELECT term, stream, code, enrols
    FROM q4_helper q
    WHERE stream = %s
    ;
"""

cur1.execute(q4_helper)
conn.commit()

if (len(sys.argv) == 1):
    cur1.execute(q4, ["ENGG"])
else:
    cur1.execute(q4, [sys.argv[1]])

prev = None
for record in cur1.fetchall():
    if (prev != record[0]):
        print(record[0])
        prev = record[0]
    print(" "+str(record[2])+"("+str(record[3])+")")



cur1.close()
conn.close()
